#!/usr/bin/env python3
import tkinter as tk
from tkinter import font
import random
import string


root = tk.Tk()
root.geometry('840x1300')
root.title('Eye Exam')
root.resizable(False, False)
root.configure(background='White')
root.grid_propagate(0)


for i in range(2):
    root.columnconfigure(i, weight=1)
for i in range(11):
    root.rowconfigure(i, weight=1)

font_type_list = ['Courier', 'FreeSerif', 'Gothic', 'Purisa', 'Waree']
font_size_list = []
grid_list = [] 

font_type = tk.StringVar()
font_type.set('FreeSerif')
font_size = 160

class char:

    def __init__(self, char, case, font):
        self.char = char
        self.case = case
        self.font = font
    
    def do_rand_letter(char):

        if char == 'Upper':
            create_letter = random.choice(string.ascii_uppercase)
        elif char == 'Lower':
            create_letter = random.choice(string.ascii_lowercase)
        else:
            create_letter = random.choice(string.ascii_letters)
          
        return create_letter

    def do_rand_number():

        create_number = random.randint(0, 9)

        return create_number
    
    def do_char_list():

        char_list = []

        for i in range(45):
            char_list.append(char.do_rand_letter('Upper'))

        return char_list

    def do_grid_index():

        grid_index = [1, 3, 6, 10, 15, 21, 28, 36, 45]
        grid_output = []
        prev = 0

        list = char.do_char_list()

        for index in grid_index:
            grid_output.append(list[prev:index])
            prev = index

        grid_output.append(list[prev:])

        return grid_output


class interface:

    def __init__(self):

        return

    def do_inputs(button_text, column_input, row_input, sticky_input, padx_input, command_input):

        button = tk.Button(root, text=button_text, foreground='Black', background='White', command=command_input, border=None)
        button.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input)

    def do_dropdown(dropdown_text, column_input, row_input, sticky_input, padx_input):
        global font_size, font_type, font_type_list

        dropdown = tk.OptionMenu(root, font_type, *(font_type_list))
        dropdown.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input)

        return font_type.get()

    def do_labels(font_text, foreground_input, background_input, column_input, row_input, sticky_input):

        pick_font = tk.Label(root, text=font_text, foreground=foreground_input, background=background_input)
        pick_font.grid(column=column_input, row=row_input, sticky=sticky_input)

    def do_graphics():

        green_line = tk.Canvas(root, background='Green', height=5)
        green_line.grid(column=1, row=6)

        red_line = tk.Canvas(root, background='Red', height=5)
        red_line.grid(column=1, row=10)

    def do_frame(width_input, height_input, columnspan_input, column_input, row_input):

        eye_frame = tk.Frame(root, background="light blue", width=width_input, height=height_input)
        eye_frame.grid(columnspan=columnspan_input, column=column_input, row=row_input, sticky='N')

    def do_chart_row_grid(font_size):
        global grid_list, font_size_list

        
        sub_row = 2
        char_row_num = 1

        for indice in char.do_grid_index():

            indice = str(indice).strip('{').strip('}').strip('[').strip(']').replace(',', '').replace("'",'')

            chart_grid = tk.Label(root, text=indice, font=str(f'{font_type.get()} {font_size}'), foreground='Black', background='White')
            chart_grid.grid(column=1, row=sub_row, sticky='S', padx=None)

            char_row_num += 1
            sub_row += 1

            if sub_row == 6 or sub_row == 10:
                sub_row += 1

            font_size_list.append(font_size)
            grid_list.append(chart_grid)

            font_size = int(font_size)//1.3
            font_size = int(font_size)


        print(font_size_list)

        return font_size, grid_list, font_size_list, font_type

    def do_row_numbers():

        sub_row = 2
        chart_row_num = 1

        for x in range(9):

            chart_number = tk.Label(root, text=chart_row_num, font='Calibri 20', foreground='Black', background='White')
            chart_number.grid(column=0, row=sub_row, sticky='W')

            chart_row_num += 1
            sub_row += 1

            if sub_row == 6 or sub_row == 10:
                sub_row += 1

    def do_font_size(outcome):
        global grid_list, font_size_list, font_size, font_type

        if outcome == 0:

            if max(font_size_list) < 170:
                for i in range(len(font_size_list)):
                    font_size_list[i] +=2

        elif outcome == 1:

            if min(font_size_list) > 1:
                for i in range(len(font_size_list)):
                    font_size_list[i] -=2

        font_size_list = list(map(int, font_size_list))
        print(font_type.get())

        for i, x in (zip(grid_list, font_size_list)):
            i.configure(font=(font_type.get(), x))

        print(font_size_list)

        return

    def do_reload_chart():

        for i in root.winfo_children():
            if isinstance(i, tk.Label):
                i.destroy()

        do_eye_exam()


def do_eye_exam():
    interface.do_frame(840, 31, 5, None, 0)
    interface.do_inputs('Reload', 0, 0, 'NW', 0, lambda:interface.do_reload_chart())
    interface.do_labels('Change Size Font', 'Black', 'light blue', 1, 0, 'N')
    interface.do_dropdown('Select Font', 2, 0, 'NE', 0)
    interface.do_graphics()
    interface.do_row_numbers()
    interface.do_chart_row_grid(font_size)
    interface.do_inputs('-', 1, 0, 'NE', 120, lambda: interface.do_font_size(1))
    interface.do_inputs('+', 1, 0, 'NW', 120, lambda: interface.do_font_size(0))
    

do_eye_exam()


root.mainloop()
