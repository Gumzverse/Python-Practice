import random

wins = 0
losses = 0
ties = 0
matches_played = 0

def play_game(user_choice):
    global wins, losses, ties, matches_played
    matches_played += 1
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=result)

    update_stats(result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def update_stats(result):
    global wins, losses, ties
    if result == "You win!":
        wins += 1
    elif result == "Computer wins!":
        losses += 1
    else:
        ties += 1

    update_stats_display()

def update_stats_display():
    stats_label.config(text=f"Wins: {wins}, Losses: {losses}, Ties: {ties}, Matches: {matches_played}")

def stop_game():
    root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x350")

user_label = tk.Label(root, text="Your Choice:", font=("Arial", 14))
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer Choice:", font=("Arial", 14))
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))  # Label to display the result
result_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"), width=10)
rock_button.pack(side=tk.LEFT, padx=5)  # Use padx for spacing

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), width=10)
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"), width=10)
scissors_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(root, text="Stop", command=stop_game, width=10)
stop_button.pack(pady=5, side=tk.RIGHT)

stats_label = tk.Label(root, text=f"Wins: {wins}, Losses: {losses}, Ties: {ties}, Matches: {matches_played}", font=("Arial", 12))
stats_label.pack(pady=10)

root.mainloop()