# Yerim Dia
# Introduction to Computer-Science
# November 16, 2018
# This program is a game in the from of a graphical user interface
# It is a guessing game where the user tries to find the hidden number

import random
import tkinter

root = tkinter.Tk()
root.title("Guess the Number")

number = random.randint(1, 100)


def answer_check():
    """
    This functions checks if the user guess is too low or too high and adds each guess to the total number of guesses
    :return: none
    """
    final_guesses = number_guesses.get() + 1
    number_guesses.set(final_guesses)
    user_guess = guess_value.get()
    if user_guess == number:
        guess_var.set("Congratulations")
    elif user_guess > number:
        guess_var.set("The number is too high")
    elif user_guess < number:
        guess_var.set("The number is too low")


guess_value = tkinter.IntVar()
guess_var = tkinter.StringVar()
number_guesses = tkinter.IntVar()
number_guesses.set(0)


img = tkinter.PhotoImage(file="guess-the-number-small.png")
imgLabel = tkinter.Label(root, image=img)
imgLabel.grid(row=1, column=3)

guess_label = tkinter.Label(root, text="Guess a Number from 1-100:", font="Helvetica 42 bold")
guess_label.grid(column=1, row=1)
guess_entry = tkinter.Entry(root, textvariable=guess_value)
guess_entry.grid(column=2, row=1)

guess_button = tkinter.Button(root, text="Guess", command=answer_check, font="Helvetica 32")
guess_button.grid(column=1, row=2)

result_label = tkinter.Label(root, textvariable=guess_var)
result_label.grid(column=2, row=2)

guess_statement = tkinter.Label(root)
guess_statement.grid(column=1, row=3, columnspan=2)

number_label = tkinter.Label(root, text="Number of Guesses:", font="Helvetica 22")
number_label.grid(column=1, row=4)

total_label = tkinter.Label(root, textvariable=number_guesses)
total_label.grid(column=2, row=4)

root.mainloop()
