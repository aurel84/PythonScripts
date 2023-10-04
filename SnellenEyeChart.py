#!/usr/bin/env python3
import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry('640x1300')
root.title('Eye Exam')
root.resizable(False, False)
root.configure(background='White')
root.grid_propagate(1)


class snellen_chart_gui:
    def __init__(self, button, label, menu):
        self.button = button
        self.label = label
        self.menu = menu

    def do_button(button_text, foreground_input, background_input, command_input, column_input, row_input, sticky_input, padx_input, pady_input):

        input_button = tk.Button(root, text=button_text, foreground=foreground_input, background=background_input, command=command_input)
        input_button.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input, pady=pady_input)

        return input_button

    def do_option_menu(selection_input, selection_list_input, command_input, column_input, row_input, sticky_input, padx_input, pady_input):

        input_dropdown = tk.OptionMenu(root, selection_input, *(selection_list_input), command=command_input)
        input_dropdown.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input, pady=pady_input)

        return input_dropdown

    def do_check_button(text_input, variable_input, background_input, foreground_input, column_input, row_input, sticky_input, padx_input, pady_input):

        input_checkbutton = tk.Checkbutton(root, text=text_input, variable=variable_input, background=background_input, foreground=foreground_input)
        input_checkbutton.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input, pady=pady_input)

        return input_checkbutton

    def do_label(text_input, font_input, foreground_input, background_input, column_input, row_input, sticky_input):

        input_label = tk.Label(root, text=text_input, font=font_input, foreground=foreground_input, background=background_input)
        input_label.grid(column=column_input, row=row_input, sticky=sticky_input)

        return input_label

    def do_canvas(background_color_input, width_input, height_input, column_input, row_input, padx_input, pady_input):

        input_canvas = tk.Canvas(root, background=background_color_input, width=width_input, height=height_input)
        input_canvas.grid(column=column_input, row=row_input, padx=padx_input, pady=pady_input)

        return input_canvas

    def do_frame(background_input, width_input, height_input, columnspan_input, column_input, row_input, sticky_input):

        input_frame = tk.Frame(root, background=background_input, width=width_input, height=height_input)
        input_frame.grid(columnspan=columnspan_input, column=column_input, row=row_input, sticky=sticky_input)

        return input_frame

    
class snellen_chart_input:

    def __init__(self, char, case, font):
        self.char = char
        self.case = case
        self.font = font
    
    def do_character_chart(outcome):

        prev = 0

        grid_index = [1, 3, 6, 10, 15, 21, 28, 36]
        character_list = []
        grid_output = []

        for i in range(45):
            if outcome == 0:
                character = random.choice(string.ascii_uppercase)
            elif outcome == 1:
                character =random.choice(string.ascii_lowercase)
            elif outcome == 2:
                character = random.choice(string.ascii_letters)
            elif outcome == 3:
                character = random.choice(string.ascii_uppercase + str(random.randint(0,9)))
            elif outcome == 4:
                character = random.choice(string.ascii_lowercase + str(random.randint(0,9)))
            elif outcome ==5:
                character = random.choice(string.ascii_letters + str(random.randint(0, 9)))
            else:
                character = random.randint(0, 9)

            character_list.append(character)

        for index in grid_index:
            grid_output.append(character_list[prev:index])
            prev = index

        grid_output.append(character_list[prev:])

        return grid_output

    def do_change_font_type(self):
        global grid_list, font_size_list, font_size, font_type

        for i, x in (zip(grid_list, font_size_list)):
            i.configure(font=(str(font_type.get()), x))

    def do_change_font_size(outcome):
        global grid_list, font_size_list, font_size, font_type

        if outcome == 0:

            if max(font_size_list) < 170:
                for i in range(len(font_size_list)):
                    font_size_list[i] +=2

        elif outcome == 1:

            if min(font_size_list) > 4:
                for i in range(len(font_size_list)):
                    font_size_list[i] -=2

        font_size_list = list(map(int, font_size_list))

        for i, x in (zip(grid_list, font_size_list)):
            i.configure(font=(str(font_type.get()), x))

    def do_change_char_type(self):

        new_font = font_case_list.index(font_case.get())

        for i, indice in (zip(grid_list, snellen_chart_input.do_character_chart(new_font))):
            indice = str(indice).strip('{').strip('}').strip('[').strip(']').replace(',', '').replace("'",'')

            i.configure(text=indice)

    def do_reload_chart():

        for i in root.winfo_children():
            i.destroy()
            
        do_snellen_chart()


def do_snellen_chart():
    global font_case, font_case_list, font_size, font_size_list, chart_grid, grid_list, font_type, font_type_list

    for i in range(2):
        root.columnconfigure(i, weight=1)
    for i in range(12):
        root.rowconfigure(i, weight=0)

    font_type_list = ['Courier', 'FreeSerif', 'Gothic', 'Purisa', 'Waree']
    font_case_list = ['Uppercase', 'Lowercase', 'Mixed-case', 'Uppper + Letters', 'Lower + Letters', 'Mixed + Letters', 'Letters']
    font_size_list = []
    grid_list = [] 

    font_type = tk.StringVar()
    font_type.set('FreeSerif')
    font_case = tk.StringVar()
    font_case.set('Uppercase')

    font_size = 160
    chart_row_num = 1

    snellen_chart_gui.do_frame('light blue', 640, 33, 3, 0, 0, 'N')
    snellen_chart_gui.do_frame('light blue', 640, 33, 3, 0, 1, 'N')
    snellen_chart_gui.do_label('Adjust Font Size', 'Calibri 15', 'Black', 'light blue', 1, 0, 'N')
    snellen_chart_gui.do_option_menu(font_type, font_type_list, snellen_chart_input.do_change_font_type, 2, 0, 'NE', None, None)
    snellen_chart_gui.do_option_menu(font_case, font_case_list, snellen_chart_input.do_change_char_type, 1, 1, 'S', None, None)
    snellen_chart_gui.do_button('-', 'Black', 'White', lambda: snellen_chart_input.do_change_font_size(1), 1, 0, 'NW', 70, None)
    snellen_chart_gui.do_button('+', 'Black', 'White', lambda: snellen_chart_input.do_change_font_size(0), 1, 0, 'NE', 70, None)
    snellen_chart_gui.do_button('Reload', 'Black', 'White', lambda: snellen_chart_input.do_reload_chart(), 0, 0, 'NW', 0, None)
    snellen_chart_gui.do_canvas('Green', 300, 5, 1, 6, 6, None)
    snellen_chart_gui.do_canvas('Red', 250, 5, 1, 10, 10, None)

    sub_row = 2

    for indice in snellen_chart_input.do_character_chart(0):
    
        indice = str(indice).strip('{').strip('}').strip('[').strip(']').replace(',', '').replace("'",'')

        chart_grid = snellen_chart_gui.do_label(indice, f'{font_type} {font_size}', 'Black', 'White', 1, sub_row, 'S')

        sub_row += 1

        if sub_row == 6 or sub_row == 10:
            sub_row += 1

        font_size_list.append(font_size)
        grid_list.append(chart_grid)

        font_size = int(font_size)//1.3
        font_size = int(font_size)

    sub_row = 2

    for x in range(9):

        snellen_chart_gui.do_label(chart_row_num, 'Calibri 20', 'Black', 'White', 0, sub_row, 'W')

        chart_row_num += 1
        sub_row += 1

        if sub_row == 6 or sub_row == 10:
            sub_row += 1


do_snellen_chart()
root.mainloop()
