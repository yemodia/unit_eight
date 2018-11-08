import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")
f_value = tkinter.StringVar()
c_value = tkinter.StringVar()

f_label = tkinter.Label(root, text="degrees F:")
f_label.grid(column=1, row=1)
f_entry = tkinter.Entry(root, textvariable=f_value)
f_entry.grid(column=2, row=1)


c_label = tkinter.Label(root, text="degrees C:")
c_label.grid(column=1, row=2)
c_entry = tkinter.Label(root, textvariable=c_value)
c_entry.grid(column=2, row=2)


root.mainloop()
