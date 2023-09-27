from tkinter import *
import random
import string


root = Tk()
root.geometry('660x1100')
root.title('Eye Exam')
menubar = Menu(root)
choices = Menubutton(menubar)
root.configure(background='White', menu=menubar)

root.columnconfigure(index=0)
root.columnconfigure(index=1)
root.columnconfigure(index=2)
root.columnconfigure(index=3)
root.columnconfigure(index=4)
root.rowconfigure(index=1)

letter_size = 192
char_row_num = 1
sub_row = 1


class char:

    def __init__(self, char, case, font):
        self.letter = char
        self.case = case
        self.font = font
    
    def do_rand_letter(char):
        global create_letter

        if char == 'Upper':
            create_letter = random.choice(string.ascii_uppercase)
        elif char == 'Lower':
            create_letter = random.choice(string.ascii_lowercase)
        else:
            create_letter = random.choice(string.ascii_letters)
          
        return create_letter

    def do_rand_number():
        global create_number

        create_number = random.randint(0, 9)

        return create_number
    
    def do_char_list():
        global char_list

        char_list = []

        for i in range(45):
            char_list.append(char.do_rand_letter('Upper'))

        def add_spaces(arg, x):
            return int(x)*" "+arg+int(x)*" "

        char_list[0:1] = [str(add_spaces(x, .1)) for x in char_list[0:1]]
        char_list[1:3] = [str(add_spaces(x, .3)) for x in char_list[1:3]]
        char_list[3:6] = [str(add_spaces(x, .6)) for x in char_list[3:6]]
        char_list[6:10] = [str(add_spaces(x, 1)) for x in char_list[6:10]] 
        char_list[10:15] = [str(add_spaces(x, 1.5)) for x in char_list[10:15]] 
        char_list[15:21] = [str(add_spaces(x, 2.1)) for x in char_list[15:21]] 
        char_list[21:28] = [str(add_spaces(x, 2.8)) for x in char_list[21:28]] 
        char_list[28:36] = [str(add_spaces(x, 3.6)) for x in char_list[28:36]]
        char_list[36:45] = [str(add_spaces(x, 4.5)) for x in char_list[36:45]]

        return char_list

    def do_grid_index():
        global grid_index

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

        button = Button(root, text=button_text, foreground='Black', background='White', command=command_input, border=None)
        button.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input)

        return

    def do_dropdown(dropdown_text, column_input, row_input, sticky_input, padx_input):

        dropdown = Menubutton(root, text=dropdown_text, background='White', activebackground='Blue', relief='raised')
        dropdown.menu = Menu(dropdown)  
        dropdown["menu"]= dropdown.menu  

        dropdown.menu.add_checkbutton(label='Caligri', background='White')
        dropdown.menu.add_checkbutton(label='Times New Roman', background='White')

        dropdown.grid(column=column_input, row=row_input, sticky=sticky_input, padx=padx_input)

        return

    def do_labels(font_text, column_input, row_input, sticky_input):

        pick_font = Label(root, text=font_text, foreground='Black', background='white')
        pick_font.grid(column=column_input, row=row_input, sticky=sticky_input)

        return

    def do_graphics():

        green_line = Canvas(root, background='Green', height=5)
        green_line.grid(column=2, row=5)

        red_line = Canvas(root, background='Red', height=5)
        red_line.grid(column=2, row=9)

    def do_chart_grid():
        global chart_grid, letter_size, char_row_num, sub_row
        
        gen_row = char.do_char_list()

        for indice in char.do_grid_index():

            indice = str(indice).strip('{').strip('}').strip('[').strip(']').replace(',', '').replace("'",'')

            if char_row_num < 10:

                chart_number = Label(root, text=char_row_num, font='Calibri 20', foreground='Black', background='White')
                chart_number.grid(column=0, row=sub_row)

            chart_grid = Label(root, text=indice, font='Calibri '+str(letter_size), foreground='Black', background='White')
            chart_grid.grid(column=2, row=sub_row, pady=5)

            char_row_num += 1
            sub_row += 1

            if sub_row == 5:
                sub_row += 1

            elif sub_row == 9:
                sub_row += 1

            letter_size = int(letter_size)//1.5
            letter_size = int(letter_size)

        return chart_grid, sub_row, letter_size, gen_row, char_row_num


def refresh():
    global root, letter_size, char_row_num, sub_row, choices

    root.destroy()
    root = Tk()
    root.geometry('660x1100')
    root.title('Eye Exam')
    menubar = Menu(root)
    choices = Menubutton(menubar)
    root.configure(background='White', menu=menubar)

    root.columnconfigure(index=0)
    root.columnconfigure(index=1)
    root.columnconfigure(index=2)
    root.columnconfigure(index=3)
    root.columnconfigure(index=4)
    root.rowconfigure(index=1)

    letter_size = 192
    char_row_num = 1
    sub_row = 1

    interface.do_inputs('Reload Exam', 0, 0, 'W', 0, refresh)
    interface.do_labels('Change Size Font', 2, 0, 'WE')
    interface.do_inputs('-', 2, 0, 'W', 120, None)
    interface.do_inputs('+', 2, 0, 'E', 120, None)
    interface.do_dropdown('Select Font', 4, 0, 'E', 0)
    interface.do_graphics()
    interface.do_chart_grid()


    root.mainloop()


interface.do_inputs('Reload Exam', 0, 0, 'W', 0, refresh)
interface.do_labels('Change Size Font', 2, 0, 'WE')
interface.do_inputs('-', 2, 0, 'W', 120, None)
interface.do_inputs('+', 2, 0, 'E', 120, None)
interface.do_dropdown('Select Font', 4, 0, 'E', 0)
interface.do_graphics()
interface.do_chart_grid()


root.mainloop()
