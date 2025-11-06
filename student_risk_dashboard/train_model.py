# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. डेटा लोड और मर्ज करें
attendance_df = pd.read_csv('data/attendance.csv')
scores_df = pd.read_csv('data/scores.csv')
fees_df = pd.read_csv('data/fees.csv')

# सभी डेटाफ्रेम को StudentID पर मर्ज करें
df = pd.merge(attendance_df, scores_df, on='StudentID')
df = pd.merge(df, fees_df, on='StudentID')

# 2. फ़ीचर इंजीनियरिंग (डेटा को मॉडल के लिए तैयार करना)
# 'FeesPaid' को संख्यात्मक बनाएं (Yes=1, No=0)
df['FeesPaid'] = df['FeesPaid'].apply(lambda x: 1 if x == 'Yes' else 0)

# जोखिम स्तर (Risk Level) को परिभाषित करने के लिए नियम बनाएं
def define_risk(row):
    if row['Attendance'] < 60 and row['Score'] < 50:
        return 2  # High Risk
    elif row['Attendance'] < 75 or row['Score'] < 60 or row['FeesPaid'] == 0:
        return 1  # Medium Risk
    else:
        return 0  # Low Risk

df['RiskLevel'] = df.apply(define_risk, axis=1)

# 3. मॉडल के लिए फ़ीचर्स और टारगेट चुनें
features = ['Attendance', 'Score', 'FeesPaid']
target = 'RiskLevel'

X = df[features]
y = df[target]

# 4. मॉडल को ट्रेन करें
# डेटा को ट्रेनिंग और टेस्टिंग सेट में विभाजित करने की आवश्यकता नहीं है क्योंकि यह एक डेमो है
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. प्रशिक्षित मॉडल को सेव करें
joblib.dump(model, 'student_risk_model.pkl')

print("Model trained and saved as student_risk_model.pkl")
print("\nFinal data used for training:")
print(df)