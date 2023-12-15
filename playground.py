# def add(*anything):
#     the_sum = sum(anything)
#     return the_sum
# result = add(3,4,5,6,7,6,7,8,6,8,9,9,7,8,9,7,65,7,9,6,5,67,8,98,6,56,78,9,7,6,67,89,87,56,67,89,98,6,78,9,7,6)
# print(result)


# or

def add(*anything):
    sum = 0
    for i in anything:
        sum += i
    return sum
result = add(3,4,5,6,7,6,7,8,6,8,9,9,7,8,9,7,65,7,9,6,5,67,8,98,6,56,78,9,7,6,67,89,87,56,67,89,98,6,78,9,7,6)
print(result)

""" For *args, it gives tuples while kwargs gives dictionary,anf the position gives just the number"""
# example

def food(a, *args, **kwargs):
   return
our_food = food("rice", 30,4, plaintain =  37, guava = 56)

print(our_food)

"""We use *args to tell the computer to accept any number of argumemts"""
# def add(*gggg):
#    name = [i * 2 for i in gggg if i > 3 ]
#    return name
# new = add(3,4,5,6,7,8,8,9,7,6,5,4)
# print(new)






from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



from tkinter import *

window = Tk()
window.title("My first GUI project")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 20,  "bold"))

""" without the pack object, the command would never appear on the screen"""
my_label.pack()

""" we can customize our label to any desired way we want"""
# my_label["text"] = "New Text"
my_label.config(text="Next Text")

def click_button():
    dan = input.get()
    my_label.config(text=dan)




"""we can actually put a button if we want"""
button = Button(text="Clck Me", command=click_button)
button.pack()

input = Entry(width=10)
input.pack()
