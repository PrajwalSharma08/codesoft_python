
from flask import Flask, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('student_risk_model.pkl')

def get_student_data_with_predictions():
    attendance_df = pd.read_csv('data/attendance.csv')
    scores_df = pd.read_csv('data/scores.csv')
    fees_df = pd.read_csv('data/fees.csv')
    
    df = pd.merge(attendance_df, scores_df, on='StudentID')
    df = pd.merge(df, fees_df, on='StudentID')
    
    df_features = df.copy()
    df_features['FeesPaid'] = df_features['FeesPaid'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    features_for_model = df_features[['Attendance', 'Score', 'FeesPaid']]
    
    predictions = model.predict(features_for_model)
    
    df['RiskPrediction'] = predictions
    
    risk_map = {0: 'Low', 1: 'Medium', 2: 'High'}
    df['RiskLevel'] = df['RiskPrediction'].map(risk_map)
    
    return df

@app.route('/')
def dashboard():
    students_df = get_student_data_with_predictions()
    
    # DataFrame को डिक्शनरी की लिस्ट में बदलें ताकि HTML में आसानी हो
    students = students_df.to_dict(orient='records')
    
    # नोटिफिकेशन उत्पन्न करें
    notifications = []
    for student in students:
        if student['RiskLevel'] == 'High':
            notifications.append(f"ALERT: High risk detected for {student['StudentName']} (ID: {student['StudentID']}). Mentor notified.")
    
    return render_template('dashboard.html', students=students, notifications=notifications)

if __name__ == '__main__':
    app.run(debug=True)