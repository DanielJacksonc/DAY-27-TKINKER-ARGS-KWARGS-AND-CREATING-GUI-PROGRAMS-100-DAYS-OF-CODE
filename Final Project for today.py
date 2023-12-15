""" we are to build  an app that converts miles to kilometers."""
#  import tkinker
from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    my_km.config(text=f'{km}')
#     # round_n = round(n, 2)
#     # result.config(text=round_n)


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=30, pady=30)

my_mile = Label(text="Miles")
my_mile.grid(column=2, row=0)

my_equal = Label(text="is equal to")
my_equal.grid(column=0,row=1)

my_km = Label(text="0")
my_km.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

my_button = Button(text="Calculate", command=convert)
my_button.grid(column=1, row=2)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)



window.mainloop()



