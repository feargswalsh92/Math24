import tkinter as tk
import parser
from random import randint

root = tk.Tk()
root.title('Math24')

###### Constants
##
FONT_LARGE = ("Calibri", 32)      ## selects the font of the text inside buttons
FONT_MED = ("Calibri", 28)
MAX_ROW = 4                        ## Max rows and columns in the GUI
MAX_COLUMN = 6
i = 0       ## for the insertion counter in Entry widget
###############

def factorial(operator):
    """Calculates the factorial of the number entered."""
    number = int(display.get())
    fact = 1
    try:
        while number > 0:
            fact = fact*number
            number -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, tk.END)

def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")


for row in range(MAX_ROW):
    root.columnconfigure(row,pad=3)

for column in range(MAX_COLUMN):
    root.rowconfigure(column,pad=3)

display = tk.Entry(root, font = ("Calibri", 32))
display.grid(row = 1, columnspan = 6 , sticky = tk.W + tk.E )

n1 = randint(0,13)
n2 = randint(0,13)
n3 = randint(0,13)
n4 = randint(0,13)

one = tk.Button(root, text = str(n1), command = lambda : get_variables(n1), font=FONT_LARGE)
one.grid(row = 2, column = 0)
two = tk.Button(root, text = str(n2), command = lambda : get_variables(n2), font=FONT_LARGE)
two.grid(row = 2, column = 1)
three = tk.Button(root, text = str(n3), command = lambda : get_variables(n3), font=FONT_LARGE)
three.grid(row = 2, column = 2)

four = tk.Button(root, text = str(n4), command = lambda : get_variables(n4), font=FONT_LARGE)
four.grid(row = 2 , column = 3)
five = tk.Button(root, text = "reset", command = clear_all, font=FONT_LARGE, foreground = "red")
five.grid(row = 2, column = 4)
six = tk.Button(root, text = "quit", font=FONT_LARGE)
six.grid(row = 2, column = 5)


plus = tk.Button(root, text = "+", command =  lambda : get_operation("+"), font=FONT_LARGE)
plus.grid(row = 3, column = 0)
minus = tk.Button(root, text = "-", command =  lambda : get_operation("-"), font=FONT_LARGE)
minus.grid(row = 3, column = 1)
multiply = tk.Button(root,text = "*", command =  lambda : get_operation("*"), font=FONT_LARGE)
multiply.grid(row = 3, column = 2)
divide = tk.Button(root, text = "/", command = lambda :  get_operation("/"), font=FONT_LARGE)
divide.grid(row = 3, column = 3)

# adding new operations

left_bracket = tk.Button(root, text = "(", command = lambda: get_operation("("), font =FONT_LARGE)
left_bracket.grid(row = 3, column = 4)

## To be added :
# sin, cos, log, ln

right_bracket = tk.Button(root, text = ")", command = lambda: get_operation(")"), font =FONT_LARGE)
right_bracket.grid(row = 3, column = 5)

nextGame = tk.Button(root, text = "Next", font=FONT_LARGE)
nextGame.grid(row = 4, column = 1)

solution = tk.Button(root, text = "solution", font=FONT_LARGE)
solution.grid(row = 4, column = 5)

result = tk.Button(root, text = "=", command = calculate, font=FONT_LARGE, foreground = "red")
result.grid(row = 4, column = 3)





root.mainloop()
