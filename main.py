from tkinter import *

def click_button():
    dan = input.get()
    my_label.config(text=dan)

window = Tk()
window.title("My first GUI project")
window.minsize(width=500, height=300)
""" We use padding to create more space around our windows or our widgets so that they are not clustered together"""
window.config(padx=10,pady=10)

my_label = Label(text="I am a label", font=("Arial", 20,  "bold"))
my_label.config(text="Next Text")

""" without the pack object, the command would never appear on the screen"""
my_label.grid(column=0, row=0)

""" we can customize our label to any desired way we want"""
# my_label["text"] = "New Text"







"""we can actually put a button if we want"""
button = Button(text="Clck Me", command=click_button)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)
new_button = Button(text="New Button", command="This is the new Button")
new_button.grid(column=2, row=0)








window.mainloop()



