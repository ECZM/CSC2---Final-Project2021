####################################################################################
###This program is so we can keep track of customer hiring for Julie's Party Hire###
####################################################################################

#import tkinter so we can make a GUI
from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the hired items
def print_hired_details ():
    #these are the global variables that are used
    global total_entries, name_count
    name_count = 0
    #Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Customer Name").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Item Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="No. of Items Hired").grid(column=4,row=7)
    #add each item in the list into its own row
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(hired_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(hired_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(hired_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(hired_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1
        
#Check the inputs are all valid
def check_inputs ():
    #these are the global variables that are used
    global hired_details, entry_customer,entry_receipt,entry_item,entry_numhired, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #Check that customer name is not blank and specific for string, set error text if blank   
    if len(entry_customer.get()) == 0 :
        Label(main_window,fg="red", text="*Required") .grid(column=2,row=0)
        input_check = 1
    elif (entry_customer.get().isdigit()) : 
        if  int(entry_customer.get()) <=0 or  int(entry_customer.get()) >=0:
            Label(main_window,fg="red", text="*Invalid") .grid(column=2,row=0)
            input_check = 1
    #Check that receipt number is not blank and specific for integer, set error text if blank     
    if len(entry_receipt.get()) == 0 :
        Label(main_window,fg="red", text="*Required") .grid(column=2,row=1)
        input_check = 1 
    elif (entry_receipt.get().isdigit()) : 
        if  int(entry_receipt.get()) < 0:
            Label(main_window,fg="red", text="*6 numbers only") .grid(column=2,row=1)
            input_check = 1
    else :
        Label(main_window,fg="red", text="*Invalid") .grid(column=2,row=1)
        input_check = 1
    #Check that item hired is not blank and specific for string, set error text if blank     
    if len(entry_item.get()) == 0 :
        Label(main_window,fg="red", text="*Required") .grid(column=2,row=2)
        input_check = 1
    elif (entry_item.get().isdigit()) : 
        if  int(entry_item.get()) <=0 or  int(entry_item.get()) >=0:
            Label(main_window,fg="red", text="*Invalid") .grid(column=2,row=2)
            input_check = 1
    #Check the number of items hired is not blank, specific for integer and between 1 and 500, set error text if blank  
    if len(entry_numhired.get()) == 0 :
        Label(main_window,fg="red", text="*Required") .grid(column=2,row=3)
        input_check = 1
    elif (entry_numhired.get().isdigit()) : 
        if  int(entry_numhired.get()) < 1 or  int(entry_numhired.get()) > 500:
            Label(main_window,fg="red", text="*1-500 only") .grid(column=2,row=3)
            input_check = 1
    else :
        Label(main_window,fg="red", text="*Invalid") .grid(column=2,row=3)
        input_check = 1
    if input_check == 0 : append_name()

#add the next item hired to the list
def append_name ():
    #these are the global variables that are used
    global hired_details, entry_customer,entry_receipt,entry_item,entry_numhired, total_entries
    #append each item to its own area of the list
    hired_details.append([entry_customer.get(),entry_receipt.get(),entry_item.get(),entry_numhired.get()])
    #clear the boxes
    entry_customer.delete(0,'end')
    entry_receipt.delete(0,'end')
    entry_item.delete(0,'end')
    entry_numhired.delete(0,'end')
    total_entries +=  1

#create the buttons and labels
def setup_buttons():
    #these are the global variables that are used
    global hired_details, entry_customer, entry_receipt,entry_item,entry_numhired, total_entries, delete_item
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Name") .grid(column=0,row=0,sticky=E)
    entry_customer = Entry(main_window)
    entry_customer.grid(column=1,row=0)
    Label(main_window, text="Receipt Number") .grid(column=0,row=1,sticky=E)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=1,row=1)
    Label(main_window, text="Item Hired") .grid(column=0,row=2,sticky=E)
    entry_item = Entry(main_window)
    entry_item.grid(column=1,row=2)
    Label(main_window, text="No. of Items Hired") .grid(column=0,row=3,sticky=E)
    entry_numhired = Entry(main_window)
    entry_numhired.grid(column=1,row=3)
    Button(main_window, text="Quit",command=quit,width = 10) .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Append Details",command=check_inputs) .grid(column=3,row=1)
    Button(main_window, text="Print Details",command=print_hired_details,width = 10) .grid(column=4,row=1,sticky=E)
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=4,row=2)
    Button(main_window, text="Delete Row",command=delete_row,width = 10) .grid(column=4,row=3,sticky=E)
    Label(main_window, text="               ") .grid(column=2,row=0)

#start the program running
def main():
    #these are the global variables that are used
    global main_window
    global hired_details, total_entries
    #create empty list for hired details and empty variable for entries in the list
    hired_details = []
    total_entries = 0
    #create the GUI and start it up
    main_window =Tk()
    main_window.title("Julie's Party Hire")
    main_window.geometry("680x600")

    setup_buttons()   
    main_window.mainloop()
    
main()