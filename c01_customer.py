####################################################################################
###This program is so we can keep track of customer hiring for Julie's Party Hire###
####################################################################################

#import tkinter so we can make a GUI
from tkinter import *

#Check the inputs are all valid
def check_inputs ():
    #these are the global variables that are used
    global entry_customer
    Label(main_window, text="               ") .grid(column=2,row=0)
    #Check that customer name is not blank and specific for string, set error text if blank   
    if len(entry_customer.get()) == 0 :
        Label(main_window,fg="red", text="*Required") .grid(column=2,row=0)
    elif (entry_customer.get().isdigit()) : 
        if  int(entry_customer.get()) <=0 or  int(entry_customer.get()) >=0:
            Label(main_window,fg="red", text="*Invalid") .grid(column=2,row=0)
       

#create the buttons and labels
def setup_buttons():
    #these are the global variables that are used
    global entry_customer
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Name") .grid(column=0,row=0,sticky=E)
    entry_customer = Entry(main_window)
    entry_customer.grid(column=1,row=0)


#start the program running
def main():
    #these are the global variables that are used
    global main_window
    #create the GUI and start it up
    main_window =Tk()
    main_window.title("Julie's Party Hire")
    main_window.geometry("680x600")

    setup_buttons()   
    main_window.mainloop()
    
main()