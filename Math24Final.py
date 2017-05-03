from tkinter import *
import tkinter as tk
import parser
from random import randint
import array
import itertools
from tkinter import messagebox
from LB_Pkg.LB_Func import LDR
from LB_Pkg.LB_Func import MessageBox
import time

winsCount=0
lossesCount=0

class Math24Solver():
    def _calculateEquation(self, lhs: object, operation: object, rhs: object):    #-> object:
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


                #test
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

location = LDR.init_DB_CWD() #Path to location of leaderboard database file (current working directory)

if  LDR.checkIfHighScore(location,winsCount):
    name = MessageBox.mbox('Congratulation!!!\n New High Score '+str(winsCount)+'\n\nEnter your name', "ok", "cancel",True,False,True)
    #function that adds leaders name and score to database file
    LDR.appendToLeaderBoard(location, name, winsCount) #function that adds leaders name and score to data file

#Leaderboard window setup
lb = tk.Tk()
lb.title('LeaderBoard')
lb.attributes('-alpha', 0.9) #gives window a transparent appearance

lb.withdraw()#hides the leaderboard window

lbframe = tk.Frame(lb,  padx =8, pady = 8)
lbframe.grid(column=0, row=0, sticky=(N, W, E, S))
lbframe.columnconfigure(0, weight=1)
lbframe.rowconfigure(0, weight=1)



#button command for revealing leaderboard gui
def viewLB(*args):
    lb.deiconify()
    i = 3 #variable that controls leaderboard name, score rows
    topten = 0 #variable controls number of leader to print
    LeaderBoardList = LDR.sortLeaderBoard(location) #return sorted list of leaders from database file
    tk.Label(lbframe, text='Rank, Name, Score', font=("Calibri", 16)).grid(column=3, row=2, sticky=W)

    #prints top ten leaders to the leaderboard gui
    for leader in LeaderBoardList:
        if topten<=9:
            tk.Label(lbframe, text=str(topten+1)+', '+leader[0]+', '+str(leader[1]), font=("Calibri", 16), relief = GROOVE).grid(column=3, row=i, sticky=W)
            i=i+1
            topten = topten+1
        else:
            break
 #button command for hiding leaderboard gui  
def hideLB(*args):
    lb.withdraw()


###### Constants
##
FONT_LARGE = ("Calibri", 16)        ## selects the font of the text inside buttons
FONT_MED = ("Calibri", 16)
MAX_ROW = 6                           ## Max rows and columns in the GUI
MAX_COLUMN = 8
PADSIZE = 8
i = 0                                 ## for the insertion counter in Entry widget
HARD = 10                             ## You can define how long you give for each set. For example, 10 second for hard level
EASY = 20                             ## You can define how long you give for each set. For example, 60 second for easy level

lastInputOperator = True            ## if last input is operator, it is true, you can input number; else it is false, and you can not input number.
numberUsed = 0                      #Make sure that all four number will be used
timeRunning = FALSE                 #Set variable then you can find way to stop timer
timeLost = FALSE                    #If your time is up, you lost one game, lossesCount will not increase if you click solution


#Top display

display = tk.Entry(root, font = ("Calibri", 32),bd = 20, insertwidth = 1)
display.grid(row = 1, columnspan = 6 , sticky = tk.W )

gameTimer = Label(root, text='Timer', fg='green', bg='black')
gameTimer.config(font=('Courier', 34))
gameTimer.grid (row =1, column = 5, columnspan = 4, sticky = tk.E + tk.W)

def timeStart():
    # if new game start, timeStart to counting down.
    global totalTime, stopwatch,timeRunning, lossesCount, numberButton, nextGame, timeLost
    # if timer starts counting down, change timeRuninning to True
    timeRunning = TRUE
    #if your left time is more than 0, continuesly update timerstart
    if (totalTime >= 0):
        gameTimer.config(text = str(totalTime))
        stopwatch = root.after(1000,timeStart)
    #if time is up, losses count is increased by 1, and it will not increase if you click solution.
    # Same time, all number buttons will be disabled.
    else:
        display.insert(8, "   You lost!")
        timeLost = TRUE
        lossesCount += 1
        lossesLabelText.set("Losses: " + str(lossesCount))
        reset.config(state = "disabled")
        for i in range(4):
            numberButton[i].config(state="disabled")
        nextGame.config(state="active")
    totalTime -= 1

#card images

Card0 = tk.PhotoImage(file = "C0.png")
Card1 = tk.PhotoImage(file = "C1.png")
Card2 = tk.PhotoImage(file = "C2.png")
Card3 = tk.PhotoImage(file = "C3.png")
Card4 = tk.PhotoImage(file = "C4.png")
Card5 = tk.PhotoImage(file = "C5.png")
Card6 = tk.PhotoImage(file = "C6.png")
Card7 = tk.PhotoImage(file = "C7.png")
Card8 = tk.PhotoImage(file = "C8.png")
Card9 = tk.PhotoImage(file = "C9.png")
Card10 = tk.PhotoImage(file = "C10.png")
Card11 = tk.PhotoImage(file = "C11.png")
Card12 = tk.PhotoImage(file = "C12.png")
Card13 = tk.PhotoImage(file = "C13.png")
CardImages = [Card0, Card1,Card2,Card3,Card4,Card5,Card6,Card7,Card8,Card9,Card10,Card11,Card12,Card13]

#number buttons
b1 = tk.Button(root, image = Card0, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
b1.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W + tk.E)
b2 = tk.Button(root, image = Card0, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
b2.grid(row = 2, column = 2, columnspan = 2, sticky = tk.W + tk.E)
b3 = tk.Button(root, image = Card0, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
b3.grid(row = 2, column = 4,columnspan = 2, sticky = tk.W + tk.E)
b4 = tk.Button(root, image = Card0, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
b4.grid(row = 2 , column = 6,columnspan = 2, sticky = tk.W + tk.E)
numberButton = [b1,b2,b3,b4]   # use button array to activate or deactivate buttons


#solution button
solution = tk.Button(root, text="Solution", padx=PADSIZE, pady=PADSIZE, font=FONT_LARGE, bd=20)
solution.grid(row=5, column=4, columnspan=4, sticky=tk.W + tk.E)



# Here we are not going to use factorial operation
'''
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
'''

def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, tk.END)
    global numberButton
    global lastInputOperator, numberUsed
    for index in range (4):
        numberButton[index].config(state = "active")
    lastInputOperator = True
    numberUsed = 0


def get_variables(index,num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i, numberUsed
    global lastInputOperator
    global numberButton
    if (lastInputOperator):
        display.insert(i, num)
        #single digital, display position is increased by 1
        if (num <10):
            i += 1
        #double digitals, display position is increased by 2
        else:
            i = i+2
        #disable button after you use the number, so all numbers can only be used once
        numberButton[index].config(state = "disabled")

        #you can not input another number after a number
        lastInputOperator = False
        numberUsed += 1


def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    global lastInputOperator
    length = len(operator)
    display.insert(i, operator)
    i += length
    lastInputOperator = True

'''
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
'''
global attemptAtSolution
attemptAtSolution=False

def calculate():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    global winsCount,lossesCount,lastInputOperator, numberButton,attemptAtSolution, numberUsed, stopwatch, nextGame
    if (numberUsed == 4):
        whole_string = display.get()
        try:
            formulae = parser.expr(whole_string).compile()
            result = eval(formulae)
            clear_all()
            attemptAtSolution=True
            if (result == 24):
                display.delete(0, tk.END)
                display.insert(0, "24      You won!")
                winsCount+=1
                winLabelText.set("Wins: "+str(winsCount))
                reset.config(state = "disabled")
                nextGame.config(state="active")
                root.after_cancel(stopwatch)

                #disable number buttons after you win this set, so you cannot repeat it over and over again
                for i in range(4):
                    numberButton[i].config(state = "disabled")

            else:
                display.insert(0, "%.2f" % result)
                display.insert(8, "   You lost!")
                lossesCount+=1
                lossesLabelText.set("Losses: "+str(lossesCount))


            #clear_all()
            #display.insert(0, result)
            lastInputOperator = False

        except Exception:
            clear_all()
            display.insert(0, "Error!")
            lastInputOperator = False


def closeWindow():
    exit()



def getNumbers():
    a=[0,0,0,0]
    for i in range(4):
        a[i]=randint(1,13)
    return a

def gameHelp():
        gameInstructions="This game is easy to learn.All you have to do is to use any of the arithmetic operations to get the four numeric values that are presented to result in the value 24." \
                         "All four numbers must be used and each number can be used only once. You can use 'C' button to restart current set. If you get stuck, click the solution button to reveal the answer." \
                         "Each game you have 20 seconds to solve the problem."
        messagebox.showinfo(title="Game Instructions", message=gameInstructions)

def newGame():

    global b1,b2,b3,b4
    global numberButton
    global result, reset, nextGame
    global attemptAtSolution
    global totalTime, stopwatch

    global numberUsed

    numberUsed = 0

    totalTime = EASY
    if (timeRunning):
        root.after_cancel(stopwatch)

    timeStart()

    result.config(state = "active")
    reset.config(state = "active")
    solution.config(state = "active")
    nextGame.config(state = "disabled")
    def displaySolution():
        global results, lossesCount, timeLost
        clear_all()
        display.insert(0, solutionString)

        if (timeRunning):
            root.after_cancel(stopwatch)

        #if you click sulotion, then you fail in this set. Your lossesCount will be increased by one only
        #if you press it in before you attempt a solution and press the "=" sign to evaluate the solution
        if(attemptAtSolution==False):
            if not timeLost:
                lossesCount+=1
        nextGame.config(state="active")

        lossesLabelText.set("Losses: "+str(lossesCount))

        #One you click sultion, all number buttons and equal button will be disabled, avoiding re-enter solution to get win-ponit
        #You can only restart new game to activate all buttons
        for i in range(4):
            numberButton[i].config(state = "disabled")
            result.config(state = "disabled")

        #disable the solution button to prevent repeated clicks before starting a new game
        solution.config(state = "disabled")
    clear_all()
    numbers = getNumbers()
    attemptAtSolution=False
    #Call Math24Solver to find out if there are solutions for these numbers
    solver = Math24Solver()

    #If there is no solution, generate another set of numbers
    while (solver.solve(numbers) == "No Solutions"):
        numbers = getNumbers()
    #First row, four numbers
    n1 = numbers[0]
    n2 = numbers[1]
    n3 = numbers[2]
    n4 = numbers[3]
    b1 = tk.Button(root, text = str(numbers[0]), image = CardImages[n1], command = lambda : get_variables(0,numbers[0]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    b1.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W + tk.E)
    b2 = tk.Button(root, text = str(numbers[1]), image = CardImages[n2],command = lambda : get_variables(1,numbers[1]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    b2.grid(row = 2, column = 2, columnspan = 2, sticky = tk.W + tk.E)
    b3 = tk.Button(root, text = str(numbers[2]), image = CardImages[n3],command = lambda : get_variables(2,numbers[2]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    b3.grid(row = 2, column = 4,columnspan = 2, sticky = tk.W + tk.E)
    b4 = tk.Button(root, text = str(numbers[3]), image = CardImages[n4],command = lambda : get_variables(3,numbers[3]), padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
    b4.grid(row = 2 , column = 6,columnspan = 2, sticky = tk.W + tk.E)

    numberButton = [b1,b2,b3,b4]

    solutionString = solver.solve(numbers)
    solution.config(command=displaySolution)


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

#Third row, record win-num and lost-num
winLabelText = tk.StringVar()
winLabel = tk.Label( root, textvariable=winLabelText, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, foreground = "green")
winLabelText.set("Wins: "+str(winsCount))
winLabel.grid(row = 4, column = 0, columnspan = 4, sticky = tk.W + tk.E)
lossesLabelText = tk.StringVar()
lossesLabel = tk.Label( root, textvariable=lossesLabelText, padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, foreground = "red")
lossesLabelText.set("Losses: "+str(lossesCount))
lossesLabel.grid(row = 4, column = 4, columnspan = 4, sticky = tk.W + tk.E)


#Fourth row, record win-num and lost-num
nextGame = tk.Button(root, text = "New Game", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
nextGame.config(command=newGame)
nextGame.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W + tk.E)


#Fifth row, record win-num and lost-num
Quit = tk.Button(root, text = "Quit", padx = PADSIZE, pady = PADSIZE, font=FONT_LARGE, bd = 20)
Quit.config(command=closeWindow)
Quit.grid(row = 6, column = 2, columnspan = 4, sticky = tk.W + tk.E)



#6th row, Leaderboard button
tk.Button(root, text="View LeaderBoard", command=viewLB).grid(column=3, row=7, sticky=W)
tk.Button(root, text="Hide LeaderBoard", command=hideLB).grid(column=4, row=7, sticky=W)

# create a pulldown menu, and add it to the menu bar
menubar = tk.Menu(root)
root.config(menu = menubar)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Game",command=newGame)
filemenu.add_command(label="Exit", command=closeWindow)

aboutMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutMenu)

helpMenu = tk.Menu(menubar, tearoff=0)
aboutMenu.add_cascade(label="Help",menu=helpMenu)


helpMenu.add_command(label="Game Instructions", command=gameHelp)









root.mainloop()
