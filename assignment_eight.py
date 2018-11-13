import tkinter
import random

root = tkinter.Tk()
root.title("Guess the Number")

number = random.randint(1, 100)
total_guesses = 0

def answer_check():
    user_guess = guess_value.get()
    if user_guess == number:
        guess_var.set("Congratulations")
    elif user_guess>number:
        guess_var.set("The number is too high")
    elif user_guess<number:
        guess_var.set("The number is too low")





guess_value = tkinter.IntVar()
guess_var = tkinter.StringVar()
number_guesses = tkinter.StringVar()
number_guesses.set(0)

guess_label = tkinter.Label(root, text="Guess a Number from 1-100:")
guess_label.grid(column=1, row=1)
guess_entry = tkinter.Entry(root, textvariable=guess_value)
guess_entry.grid(column=2, row=1)

guess_button = tkinter.Button(root, text="Guess", command=answer_check)
guess_button.grid(column=1, row=2)

result_label = tkinter.Label(root, textvariable=guess_var)
result_label.grid(column=2, row=2)

guess_statement = tkinter.Label(root)
guess_statement.grid(column=1, row=3, columnspan=2)

number_label = tkinter.Label(root, text="Number of Guesses:")
number_label.grid(column=1, row=4)

total_label = tkinter.Label(root, textvariable=number_guesses)
total_label.grid(column=2, row=4)

root.mainloop()
