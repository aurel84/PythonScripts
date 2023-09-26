from tkinter import *
import random
import string

root = Tk()
root.geometry('600x1200')
root.title('Eye Exam')
root.configure(background='White')

letter_size = 192
char_row_num = 1
sub_row = 1
padding = 2


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

        def add_spaces(str1, x):
            return int(x)*" "+str1+int(x)*" "

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

    def do_graphics():

        green_line = Canvas(root, background='Green', height=5)
        green_line.grid(row=5, column=2)

        red_line = Canvas(root, background='Red', height=5)
        red_line.grid(row=9, column=2)

    def do_chart_grid():
        global chart_grid
        global letter_size
        global char_row_num
        global sub_row
        
        gen_row = char.do_char_list()

        for indice in char.do_grid_index():

            indice = str(indice).strip('{').strip('}').strip('[').strip(']').replace(',', '').replace("'",'')

            if char_row_num < 10:

                chart_number = Label(root, text=char_row_num, font='Calibri 30', foreground='Black', background='White')
                chart_number.grid(column=0, row=sub_row, pady=15)

            chart_grid = Label(root, text=indice, font='Calibri '+str(letter_size), foreground='Black', background='White')
            chart_grid.grid(column=2, row=sub_row)

            char_row_num += 1
            sub_row += 1

            if sub_row == 5:
                sub_row += 1

            elif sub_row == 9:
                sub_row += 1

            letter_size = int(letter_size)//1.5
            letter_size = int(letter_size)

        return chart_grid, sub_row, letter_size, gen_row, padding, char_row_num

interface.do_graphics()
interface.do_chart_grid()

root.mainloop()
