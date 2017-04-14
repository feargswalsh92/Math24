import tkinter as tk
import parser
from random import randint
import array
import itertools
import time

class Math24Solver():
    def _calculateEquation(self, lhs, operation, rhs):
        """
        Calculates and returns the mathematical solution to the 
        equation depending on the operation
        :type lhs: int
        :type operation: str
        :type rhs: int
        :rtype: int
        """
        if operation is "+":
            return lhs + rhs
        elif operation is "-":
            return lhs - rhs
        elif operation is "*":
            return lhs * rhs
        else:
            if rhs is not 0:
                return lhs / rhs

    def _is24(self, values, op1, op2, op3):
        """
        Checks whether the complete equation equates to 24.
        :type values: List[int]
        :type op1: str
        :type op2: str
        :type op3: str
        :rtype: bool
        """
        solution = values[0]
        solution = self._calculateEquation(solution, op1, values[1])
        solution = self._calculateEquation(solution, op2, values[2])
        solution = self._calculateEquation(solution, op3, values[3])

        if solution is 24:
            return True
        else:
            return False

    def _isPlusOrMinus(self, op):
        """
        Checks whether operation is addition or subtraction
        
        :type op: str
        :rtype: bool
        """

        if op is "+" or op is "-":
            return True
        else:
            return False

    def _formatSolution(self, values, op1, op2, op3):

        """
        Formats the solution by adding parentheses to show proper
        order of operations to create 24
        Possible combinations of operations 
        (where + represents addition and subtraction tier of operations
        and * represents multiplication and division tier of operations)
        +++ -> No change
        ++* -> (++)*
        +*+ -> (+)*+
        *++ -> No change
        **+ -> No change
        *+* -> (*+)*
        +** -> (+)**
        *** -> No change
        
        :type values: List[int]
        :type op1: str
        :type op2: str
        :type op3: str
        :rtype: str
        """
        #Default solution is no change
        solution = "{}{}{}{}{}{}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        #Adding parenthesis where first operation is + or -
        if self._isPlusOrMinus(op1):
            if self._isPlusOrMinus(op2) and not self._isPlusOrMinus(op3): #Case: ++* -> (++)*
                solution = "({}{}{}{}{}){}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])
            elif not self._isPlusOrMinus(op2): #Cases: +*+ -> (+)*+  and +** -> (+)**
                solution = "({}{}{}){}{}{}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        #Adding parenthesis where the operation is *+* -> (*+)*
        else:
            if self._isPlusOrMinus(op2) and not self._isPlusOrMinus(op3): #Case: *+* ->(*+)*
                solution = "({}{}{}{}{}){}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        return solution

    def solve(self, inputValues):
        """
        Given four numbers, solves whether there is a solution that creates 24. Returns the
        solution if it exists, and returns "No Solutions" otherwise
        :type inputValues: List[int]
        :rtype: str
        """

        #List the valid operations of addition, subtraction, multiplication and division
        validOps = ["+", "-", "*", "/"]

        #Get user input for the four values from Math 24 card
        length = len(inputValues)
        if length is not 4:
            raise ValueError("Invaid number of inputs.")

        #Get permutations of the four numbers
        inputValues = itertools.permutations(inputValues)

        #Search for a solution that equal 24

        for i in inputValues:   #Go through permutations list

            for op1 in validOps:    #Go through valid operations

                for op2 in validOps:

                    for op3 in validOps:
                        if self._is24(i, op1, op2, op3):
                            return self._formatSolution(i, op1, op2, op3)

        return "No Solutions"



root = tk.Tk()
root.title('Math24')



###### Constants
##
FONT_LARGE = ("Calibri", 16)      ## selects the font of the text inside buttons
FONT_MED = ("Calibri", 16)
MAX_ROW = 6                        ## Max rows and columns in the GUI
MAX_COLUMN = 8
PADSIZE = 8
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

#def timer():

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
        if result == 24:
            display.insert(0, "You won!")
        else:
            display.insert(0, "You lost!")
        #clear_all()
        #display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")


def closeWindow():
    exit()

#Top display 
display = tk.Entry(root, font = ("Calibri", 32),bd = 20, insertwidth = 1)
display.grid(row = 1, columnspan = 8 , sticky = tk.W + tk.E )

#Create four random number between 1 and 13
'''n1 = randint(1,13)
n2 = randint(1,13)
n3 = randint(1,13)
n4 = randint(1,13)
'''


def getNumbers():
    a=[0,0,0,0]
    for i in range(4):
        a[i]=randint(1,13)
    return a


def newGame():

    def displaySolution():
        clear_all()
        display.insert(0, solutionString) 

    clear_all()
    numbers = getNumbers()

    #Call Math24Solver to find out if there are solutions for these numbers
    solver = Math24Solver()

    #If there is no solution, generate another set of numbers
    while (solver.solve(numbers) == "No Solutions"):
        numbers = getNumbers()
    #First row, four numbers
    one = tk.Button(root, text = str(numbers[0]), command = lambda : get_variables(numbers[0]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    one.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W + tk.E)
    two = tk.Button(root, text = str(numbers[1]), command = lambda : get_variables(numbers[1]), padx = PADSIZE, pady = PADSIZE,font=FONT_LARGE, bd = 20)
    two.grid(row = 2, column = 2, columnspan = 2, sticky = tk.W + tk.E)
    three = tk.Button(root, text = str(numbers[2]), command = lambda : get_variables(numbers[2]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    three.grid(row = 2, column = 4,columnspan = 2, sticky = tk.W + tk.E)
    four = tk.Button(root, text = str(numbers[3]), command = lambda : get_variables(numbers[3]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    four.grid(row = 2 , column = 6,columnspan = 2, sticky = tk.W + tk.E)


    solutionString = solver.solve(numbers)

    solution = tk.Button(root, text = "solution", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    solution.config(command=displaySolution)
    solution.grid(row = 5, column = 4, columnspan = 4, sticky = tk.W + tk.E)

newGame()


#Second row, all operators
plus = tk.Button(root, text = "+", command =  lambda : get_operation("+"), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
plus.grid(row = 3, column = 0, sticky = tk.W + tk.E)

minus = tk.Button(root, text = "-", command =  lambda : get_operation("-"), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
minus.grid(row = 3, column = 1, sticky = tk.W + tk.E)

multiply = tk.Button(root,text = "*", command =  lambda : get_operation("*"), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
multiply.grid(row = 3, column = 2, sticky = tk.W + tk.E)

divide = tk.Button(root, text = "/", command = lambda :  get_operation("/"), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
divide.grid(row = 3, column = 3, sticky = tk.W + tk.E)

left_bracket = tk.Button(root, text = "(", command = lambda: get_operation("("), padx = PADSIZE, pady = PADSIZE, font =FONT_LARGE, bd = 20)
left_bracket.grid(row = 3, column = 4, sticky = tk.W + tk.E)

right_bracket = tk.Button(root, text = ")", command = lambda: get_operation(")"), padx = PADSIZE, pady = PADSIZE, font =FONT_LARGE, bd = 20)
right_bracket.grid(row = 3, column = 5, sticky = tk.W + tk.E)

reset = tk.Button(root, text = "C", command = clear_all, font=FONT_LARGE, padx = PADSIZE, pady = PADSIZE, bd = 20)
reset.grid(row = 3, column = 6, sticky = tk.W + tk.E)

result = tk.Button(root, text = "=", command = calculate, font=FONT_LARGE, padx = PADSIZE, pady = PADSIZE, bd = 20)
result.grid(row = 3, column = 7, sticky = tk.W + tk.E)



#Third row, recod win-num and lost-num
winNum = tk.Button(root, text = "win 0", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, foreground = "red", bd = 20)
winNum.grid(row = 4, column = 0, columnspan = 4, sticky = tk.W + tk.E)

winNum = tk.Button(root, text = "lose 0", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, foreground = "green", bd = 20)
winNum.grid(row = 4, column = 4, columnspan = 4, sticky = tk.W + tk.E)


#Fourth row, recod win-num and lost-num
nextGame = tk.Button(root, text = "New Game", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
nextGame.config(command=newGame)
nextGame.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W + tk.E)


#Fifth row, recod win-num and lost-num
Quit = tk.Button(root, text = "Quit", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
Quit.config(command=closeWindow)
Quit.grid(row = 6, column = 2, columnspan = 4, sticky = tk.W + tk.E)



# create a pulldown menu, and add it to the menu bar
menubar = tk.Menu(root)
root.config(menu = menubar)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Game",command=newGame)
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=closeWindow)

aboutMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Help")
aboutMenu.add_command(label="Author")





root.mainloop()
