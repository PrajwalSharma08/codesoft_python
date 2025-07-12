import tkinter as tk
import random

# Game logic
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    update_display(user_choice, computer_choice, result)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        scores["user"] += 1
        return "user"
    else:
        scores["computer"] += 1
        return "computer"

def update_display(user, computer, result):
    user_choice_label.config(text=f"You chose: {user}")
    computer_choice_label.config(text=f"Computer chose: {computer}")
    if result == "tie":
        result_label.config(text="Result: It's a tie!", fg="blue")
    elif result == "user":
        result_label.config(text="Result: You win! 🎉", fg="green")
    else:
        result_label.config(text="Result: You lose. 😢", fg="red")

    score_label.config(
        text=f"Score - You: {scores['user']} | Computer: {scores['computer']}"
    )

# Initialize GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

scores = {"user": 0, "computer": 0}

# Title
title = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: play("rock"))
paper_btn = tk.Button(button_frame, text="📄 Paper", width=10, command=lambda: play("paper"))
scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=10, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Result display
user_choice_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
