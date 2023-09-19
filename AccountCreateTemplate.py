import random
import string
from tkinter import *

root = Tk()
root.geometry("720x540")
root.title("Account Creation Tool")
root.columnconfigure(index=0)
root.columnconfigure(index=1)
root.columnconfigure(index=2)
root.columnconfigure(index=3)
                     
input_row_selection = StringVar()
input_row_selection.set("None")
export_selection = StringVar()
export_selection.set("None")
Checkbutton1 = IntVar()
Checkbutton2 = IntVar()

total_rows = []
total_clear_buttons = []
total_destroy_buttons = []
total_passwords = []
user_list = []


def create_password(length):
    if Checkbutton1.get() and Checkbutton2.get() == 1:
        letters = string.ascii_letters + string.digits

    elif Checkbutton1.get() == 1:
        letters = string.digits + string.ascii_lowercase


    elif Checkbutton2.get() == 1:
        letters = string.ascii_letters

    else:
        letters = string.ascii_lowercase

    new_password = ''.join(random.choice(letters) for i in range(int(length)))
    total_passwords.append(new_password)

    print(total_passwords)


def print_rows():
    for i in total_rows:
        i = i.get()
        user_list.append(i)

    while('' in user_list):
        user_list.remove('')
    
    print(user_list)

def destroy_row(Input_Row, Delete_Button):
    Input_Row.destroy()
    Delete_Button.destroy()
    total_rows.remove(Input_Row)


def delete_entry(Input_Row):
    Input_Row.delete(0, END)
    

def create_rows(selection):
    new_row = 0

    if total_rows != []:
        for i in total_rows:
            i.destroy()

        for i in total_clear_buttons:
            i.destroy()

        for i in total_destroy_buttons:
            i.destroy()

    for i in range(int(selection)):
        new_row += 1

        Input_Row = str('Input_row_') + str(new_row)

        Input_Row = Entry(root, foreground='Black', background='White', width=25)
        Input_Row.grid(column=2, row=new_row, pady=5, sticky=W)

        Delete_Button = Button(root, text='Clear', foreground='Black', command=lambda b=Input_Row: delete_entry(b))
        Delete_Button.grid(column=3, row=new_row, pady=5, sticky=W)

        Destroy_Button = Button(root, text='Delete', foreground='Black', command=lambda a=Input_Row, b=Delete_Button: destroy_row(a, b))
        Destroy_Button.grid(column=4, row=new_row, pady=5, sticky=E)

        total_rows.append(Input_Row)
        total_clear_buttons.append(Delete_Button)
        total_destroy_buttons.append(Destroy_Button)

    return total_rows, total_clear_buttons, total_destroy_buttons, Input_Row, Destroy_Button, new_row


f1_left_title = Label(root, text="Configure Inputs", font='Calibri 15', foreground='Black')
f1_left_title.grid(column=0, row=0, pady=10, sticky=W)

f2_left_row_select = Label(root, text="Number of Rows:", font='Calibri 12', foreground='Black')
f2_left_row_select.grid(column=0, row=1, pady=5, sticky=W)

f2_input_row_selection = OptionMenu(root, input_row_selection, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', command=create_rows)
f2_input_row_selection.grid(column=1, row=1, pady=5, sticky=W)

f3_append_label = Label(root, text="Append at end:", font='Calibri 12', foreground='Black')
f3_append_label.grid(column=0, row=2, pady=5, sticky=W)

f3_append_entry = Entry(root, textvariable='', foreground='Black', background='White', width=15)
f3_append_entry.grid(column=1, row=2, pady=5, sticky=W)

f4_export_label = Label(root, text="Export file as:", font='Calibri 12', foreground='Black')
f4_export_label.grid(column=0, row=3, pady=5, sticky=W)

f4_export_selection = OptionMenu(root, export_selection, 'None', 'Excel', 'CSV', command='')
f4_export_selection.grid(column=1, row=3, pady=5, sticky=W)

f5_password_title = Label(root, text="Password (randomized)", font='Calibri 15', foreground='Black')
f5_password_title.grid(column=0, columnspan=1, row=4, pady=10, sticky=W)

f6_pass_length_label = Label(root, text="Character Length:", font='Calibri 12')
f6_pass_length_label.grid(column=0, row=5, pady=5, sticky=W)

f5_pass_length_menu = OptionMenu(root, input_row_selection, '8', '10', '12', '14', '16', command=create_password)
f5_pass_length_menu.grid(column=1, row=5, pady=5, sticky=W)

f7_num_checkmark_box = Checkbutton(root, variable=Checkbutton1, text='Numbers', onvalue=1, offvalue=0)
f7_num_checkmark_box.grid(column=1, row=6, pady=5, sticky=W)

f8_cap_checkmark_box = Checkbutton(root, variable=Checkbutton2, text='Capitalization', anchor=W, onvalue=1, offvalue=0)
f8_cap_checkmark_box.grid(column=0, row=6, pady=5, sticky=W)

f1_right_title = Label(root, text="Users to Import", font='Calibri 15', foreground='Black')
f1_right_title.grid(column=2, row=0, pady=10, sticky=W)

f_check_botton = Button(root, text='Export Values', foreground='Black', command=print_rows, width=40)
f_check_botton.grid(column=0, columnspan=2, row=11, pady=5)


root.mainloop()
