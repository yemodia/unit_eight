import tkinter
import random

root = tkinter.Tk()
root.title("Guess the Number")

def random_number():
    number = random.randint(1, 100)
    return number

def user_guess():

guess_value = tkinter.IntVar()
guess_statement = tkinter.StringVar()
number_guesses = tkinter.IntVar()

guess_label = tkinter.Label(root, text="Guess a Number from 1-100:")
guess_label.grid(column=1, row=1)
guess_entry = tkinter.Entry(root, textvariable=guess_value)
guess_entry.grid(column=3, row=1)

guess_button = tkinter.Button(root, text="Guess")
guess_button.grid(column=2, row=6)

guess_statement = tkinter.Label(root)
guess_statement.grid(column=2, row=8)

number_guesses = tkinter.Label(root, text="Number of Guesses:")
number_guesses.grid(column=1, row=10)

root.mainloop()
