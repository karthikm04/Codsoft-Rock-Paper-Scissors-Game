import tkinter as tk
import random
from tkinter import messagebox

# Game Logic
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_round(user_choice):
    global current_round, max_rounds
    if current_round <= max_rounds:
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            result_label.config(text=f"Computer chose {computer_choice}\n{result}", fg="green")  # Green for "You win"
        else:
            result_label.config(text=f"Computer chose {computer_choice}\n{result}", fg="white")  # Default for others
            
        update_scores(result)
        round_label.config(text=f"Round: {current_round}/{max_rounds}")
        current_round += 1
    if current_round > max_rounds:
        end_game()

def update_scores(result):
    global user_score, computer_score
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1
    score_label.config(text=f"User: {user_score}  |  Computer: {computer_score}")

def end_game():
    result_label.config(text="Game Over! Click Play Again to start.", fg="red")
    # Disable buttons
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

def play_again():
    reset_game()
    
def reset_game():
    global user_score, computer_score, current_round
    user_score = 0
    computer_score = 0
    current_round = 1
    score_label.config(text=f"User: {user_score}  |  Computer: {computer_score}")
    result_label.config(text="Make your choice!", fg="violet")  # Violet for "Make your choice!"
    round_label.config(text=f"Round: {current_round}/{max_rounds}")
    
    # Enable buttons
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

def exit_game():
    root.quit()

# User Interface
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x600")  # Larger window for full-page design
root.config(bg="#1e1e1e")  # Dark background

# Variables
user_score = 0
computer_score = 0
current_round = 1
max_rounds = 5

# Header
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 30, "bold"), fg="#FFD700", bg="#1e1e1e", relief="solid", bd=2)
title_label.pack(pady=20)

# Round Indicator - Red color
round_label = tk.Label(root, text=f"Round: {current_round}/{max_rounds}", font=("Arial", 18, "bold"), fg="red", bg="#1e1e1e", relief="solid", bd=2)
round_label.pack(pady=10)

# Result Label - Violet for "Make your choice!"
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 18, "bold"), fg="violet", bg="#1e1e1e", relief="solid", bd=2)
result_label.pack(pady=20)

# Score Display
score_label = tk.Label(root, text=f"User: {user_score}  |  Computer: {computer_score}", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#1e1e1e", relief="solid", bd=2)
score_label.pack(pady=10)

# Button Styling
def create_stylish_button(parent, text, command):
    return tk.Button(parent, text=text, font=("Arial", 14, "bold"), bg="#00BFFF", fg="white", bd=5, width=12, height=2, command=command, relief="raised", activebackground="#4682B4", activeforeground="white")

# Button Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

# Buttons
rock_button = create_stylish_button(button_frame, "Rock", lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=15)

paper_button = create_stylish_button(button_frame, "Paper", lambda: play_round("Paper"))
paper_button.grid(row=0, column=1, padx=15)

scissors_button = create_stylish_button(button_frame, "Scissors", lambda: play_round("Scissors"))
scissors_button.grid(row=0, column=2, padx=15)

# Play Again and Exit
bottom_frame = tk.Frame(root, bg="#1e1e1e")
bottom_frame.pack(pady=30)

play_again_button = create_stylish_button(bottom_frame, "Play Again", play_again)
play_again_button.grid(row=0, column=0, padx=15)

exit_button = create_stylish_button(bottom_frame, "Exit", exit_game)
exit_button.grid(row=0, column=1, padx=15)

root.mainloop()
