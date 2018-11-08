import tkinter


root = tkinter.Tk()
root.title("Guess the Number")
guess_value = tkinter.IntVar()

guess_label = tkinter.Label(root, text="Guess a Number from 1-100:")
guess_label.grid(column=1, row=1)
guess_entry = tkinter.Entry(root, textvariable=guess_value)
guess_entry.grid(column=3, row=1)

guess_button = tkinter.Button(root, text="Guess")
guess_button.grid(column=2, row=6)



root.mainloop()
