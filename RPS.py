import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def on_choice_button_click(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    update_scores(result)
    show_result_message(choice, computer_choice, result)

def update_scores(result):
    global user_score, computer_score
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1
    user_score_label.config(text=f"You: {user_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

def show_result_message(user_choice, computer_choice, result):
    messagebox.showinfo("Result", f"You chose {user_choice}. Computer chose {computer_choice}.\n{result}")

# Create the main window
root = tk.Tk()
root.title("RPS")

# Initialize scores
user_score = 0
computer_score = 0

# Load images for choices
rock_img = Image.open("C:/Users/MONSTER/Desktop/stone.png")
paper_img = Image.open("C:/Users/MONSTER/Desktop/paper.jpeg")
scissors_img = Image.open("C:/Users/MONSTER/Desktop/scissors.jpg")

# Resize images to a consistent size
img_size = (50, 50)
rock_img = rock_img.resize(img_size)
paper_img = paper_img.resize(img_size)
scissors_img = scissors_img.resize(img_size)

# Convert images to Tkinter PhotoImage objects
rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Create labels for scores
user_score_label = tk.Label(root, text=f"You: {user_score}")
computer_score_label = tk.Label(root, text=f"Computer: {computer_score}")

# Create buttons for each choice with images
rock_button = tk.Button(root, compound=tk.TOP, image=rock_photo, text="Rock", command=lambda: on_choice_button_click("rock"))
paper_button = tk.Button(root, compound=tk.TOP, image=paper_photo, text="Paper", command=lambda: on_choice_button_click("paper"))
scissors_button = tk.Button(root, compound=tk.TOP, image=scissors_photo, text="Scissors", command=lambda: on_choice_button_click("scissors"))


user_score_label.pack()
computer_score_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)


root.mainloop()
