####################################################################################
###This program is so we can keep track of customer hiring for Julie's Party Hire###
####################################################################################

#Import tkinter so we can make a GUI
from tkinter import *

my_window = Tk()
my_window.title("Julie's Party Hire")
my_window.geometry("600x600")


def exit():
    my_window.destroy()

def append():
    list = Label

def print():
    customerheading = Label(my_window, font ="Helvetica 10 bold", text ="Customer Name")
    name_of_customer = Label(my_window, text = entry_customer_name.get())
    customerheading.grid(column=0, row=2)
    name_of_customer.grid(column=0, row=3)


customer_name = Label(my_window, text ="Customer Name")
entry_customer_name = Entry(my_window)
print_button = Button(my_window, text ="Print", command =print)
append_button = Button(my_window, text ="Append Details", command =append)

customer_name.grid(column=0, row=0)
entry_customer_name.grid(column=1, row=0)
print_button.grid(column=5, row=1)



exit_button = Button(my_window, text ="Exit", command=exit)
exit_button.grid(column=5, row=0)

my_window.mainloop()