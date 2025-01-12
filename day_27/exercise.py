from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Grid")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text="More Text")
my_label.grid(column=1., row=1)

# Buttons
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=3, row=1)

button = Button(text="Button", command=button_clicked)
button.grid(column=3, row=1)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=3)


window.mainloop()
