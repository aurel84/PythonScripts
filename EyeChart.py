from tkinter import *
import random
import string

root = Tk()
root.geometry('200x480')
root.title('Eye Exam')
root.configure(background='white')

letter_size = 128


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

        for i in range(15):
            char_list.append(char.do_rand_letter('Upper'))

        return char_list


class interface:

    def do_grid_index():
        global grid_index

        grid_index = [1, 3, 7]
        grid_output = []
        prev = 0

        list = char.do_char_list()

        for index in grid_index:
            grid_output.append(list[prev:index])
            prev = index

        grid_output.append(list[prev:])

        return grid_output
    
    def do_chart_grid():
        global chart_grid
        global letter_size
        global sub_row
        
        sub_row = 1

        gen_row = char.do_char_list()

        for indice in interface.do_grid_index():

            chart_grid = Label(root, text=indice, font='Calibri '+str(letter_size)+'', foreground='Black', background='white')
            chart_grid.grid(column=0, row=sub_row, pady=10, padx=10)

            sub_row += 1
            letter_size = letter_size//2

        return chart_grid, sub_row, letter_size, gen_row


interface.do_chart_grid()


root.mainloop()
