import os.path
import string
import re
import sys
import tkinter

class LDR(object):
    """Holds all static functions for leaderboard functionality"""
    
    
    def getLeaderBoard(databasefile):
        """
        Function takes a db txt file path (string), parses all names score, and return a list
        """
        leaders = LDR.sortLeaderBoard(databasefile)
        print('LeaderBoard')
        print('Rank','Name','Score')
        rank = 1
        topten =0    
        for name, score in leaders:
            if topten<=9:
                print(rank,name,score)
                rank=rank+1
                topten=topten +1
            else:
                break  

    #Check if the score is a high score or or top ten
    def checkIfHighScore(databasefile, score):
        """
        Function takes a path to a text file, and int score, and compares 
        all items of the text file to the int score and returns true or false
        """
        if score<1:
            return False
        #conditions that check if file is empty
        if  LDR.checkIfDataBaseFileIsEmpty(databasefile):
            return True
        LDR.sortLeaderBoard(databasefile) #sort leaderboard
        LeaderBoardDataBaseFile = open(databasefile) #open leaderboard file
        i = 0 #track iteration thru leaders of the leaderboard
        
        try:#store top 10 leaders on the sorted leaderboard
            LeaderBoardParseList = [] #creates list
            for CurrentLine in LeaderBoardDataBaseFile:#iterate thru leaders
                linesplit = CurrentLine.split(",") #creates tuples name,score
                currentscore = int(linesplit[1])#store and convert current string score to int
                LeaderBoardParseList.append((currentscore)) #append current int score to list
                ++i
                if i==10:
                    break
        finally:
            LeaderBoardDataBaseFile.close()#close db file
        for entry in LeaderBoardParseList: #iterates thru the top 10 leaders
            if (i<10) or (score>entry):#compares score with top ten leaders considering number of leaders
                return True
            
        return False
    #Function that sorts leaderboard database file
    def sortLeaderBoard(databasefile):
        """
        Function takes representation of a string text file path sort all the items by int size
        """
        LeaderBoardDataBaseFile = open(databasefile)
        try:
            LeaderBoardParseList = [] #creates list
            for CurrentLine in LeaderBoardDataBaseFile:
                linesplit = CurrentLine.split(",") #creates tuples 
                name = linesplit[0]
                score = int(linesplit[1])
                LeaderBoardParseList.append((name,score)) #adds tuples to list
        finally:
            LeaderBoardDataBaseFile.close()
            LeaderBoardDataBaseFile = open(databasefile,"w")#opens the database file in write mode then closes to clear content
            LeaderBoardDataBaseFile.close()
        leaders = sorted(LeaderBoardParseList, key = lambda lead: lead[1], reverse = True) #sorts list of tuples
        for CurrentTuple in leaders:
                
            LDR.appendToLeaderBoard(databasefile, CurrentTuple[0], CurrentTuple[1])
        return leaders 
    
    #Function takes a db text file path (string), name and score, overwrite file
    def overWriteLeaderBoard(databasefile, name, score):
        """
        Function takes a string file path, string name, int and write to file
        """
        LeaderBoardDataBaseFile = open(databasefile, "w")
        try:
            leader = name+','+str(score)+'\n'
            LeaderBoardDataBaseFile.write(leader)
        finally:
            LeaderBoardDataBaseFile.close()
           
    #Append Leader name and score to leaderboard
    def appendToLeaderBoard(databasefile, name, score):
        """
        Function takes a string file path, string name int score, adds a new line to the file containing 
        name and score
        """
        LeaderBoardDataBaseFile = open(databasefile, "a")
        try:
            leader = name+','+str(score)+'\n'
            LeaderBoardDataBaseFile.write(leader)
        finally:
            LeaderBoardDataBaseFile.close()

    #Check if database is empty
    def checkIfDataBaseFileIsEmpty(pathstring):
        """
        Function takes a string file path and check if file is empty returns bool
        """
        LeaderBoardDataBaseFile = open(pathstring)
        if  LeaderBoardDataBaseFile.readline() == "":
            LeaderBoardDataBaseFile.close()
            return True
        else:
            return False

    #Check if database txt file exists
    def checkIfDataBaseFileExist(pathstring):
        """
        Function takes a string file path and check if file exists, returns a bool
        """
        if os.path.isfile(pathstring):
           return True
        else:
           return False

    #Intializes database file location to the current working directory
    def init_DB_CWD():
        """
        Function initializes the file and location to the running script working directory
        returns a string representation of the initialized file and location
        """
        #creates string containing the database file and working directory
        location = os.path.dirname(os.path.realpath(sys.argv[0]))+"\\Ldr_Brd_DB.csv" 
        if LDR.checkIfDataBaseFileExist(location): #if exist return string representation
            return location
        else: #else creates the database txt file and places it in the current working directory
            LeaderBoardDataBaseFile = open(location,'w') 
            LeaderBoardDataBaseFile.close()
            return location
        
    #Check if databse is full(10 Leaders)
    def checkIfDataBaseFileIsFull(pathstring):
        """
        Function takes a string file path and check if reached max length size, returns bool
        """
        LeaderBoardDataBaseFile = open(pathstring)
        count=0
        for line in LeaderBoardDataBaseFile:
            count = count+1
        if  count>=10:
            LeaderBoardDataBaseFile.close()
            return True
        else:
            LeaderBoardDataBaseFile.close()
            return False  
#Message box for leaderboard user prompt
class MessageBox(object):
    """
    Object contains implementation for a seperate frame independant of root
    for leaderboard user prompt
    """    
    def __init__(self, msg, b1, b2, frame, t, entry):

        root = self.root = tkinter.Tk()
        root.title('High Score')
        self.msg = str(msg)
        # ctrl+c to copy self.msg
        root.bind('<Control-c>', func=self.to_clip)
        # remove the outer frame if frame=False
        if not frame: root.overrideredirect(True)
        # default values for the buttons to return
        self.b1_return = True
        self.b2_return = False
        # if b1 or b2 is a tuple unpack into the button text & return value
        if isinstance(b1, tuple): b1, self.b1_return = b1
        if isinstance(b2, tuple): b2, self.b2_return = b2
        # main frame
        frm_1 = tkinter.Frame(root)
        frm_1.pack(ipadx=2, ipady=2)
        # the message
        message = tkinter.Label(frm_1, text=self.msg)
        message.pack(padx=8, pady=8)
        # if entry=True create and set focus
        if entry:
            self.entry = tkinter.Entry(frm_1)
            self.entry.pack()
            self.entry.focus_set()
        # button frame
        frm_2 = tkinter.Frame(frm_1)
        frm_2.pack(padx=4, pady=4)
        # buttons
        btn_1 = tkinter.Button(frm_2, width=8, text=b1)
        btn_1['command'] = self.b1_action
        btn_1.pack(side='left')
        if not entry: btn_1.focus_set()
        btn_2 = tkinter.Button(frm_2, width=8, text=b2)
        btn_2['command'] = self.b2_action
        btn_2.pack(side='left')
        # the enter button will trigger the focused button's action
        btn_1.bind('<KeyPress-Return>', func=self.b1_action)
        btn_2.bind('<KeyPress-Return>', func=self.b2_action)
        # roughly center the box on screen
        # for accuracy see: http://stackoverflow.com/a/10018670/1217270
        root.update_idletasks()
        xp = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        yp = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        geom = (root.winfo_width(), root.winfo_height(), xp, yp)
        root.geometry('{0}x{1}+{2}+{3}'.format(*geom))
        # call self.close_mod when the close button is pressed
        root.protocol("WM_DELETE_WINDOW", self.close_mod)
        # a trick to activate the window (on windows 7)
        root.deiconify()
        # if t is specified: call time_out after t seconds
        if t: root.after(int(t*1000), func=self.time_out)

    def b1_action(self, event=None):#defines action on button 1
        try: x = self.entry.get()#assigns entry to variable
        except AttributeError:
            self.returning = self.b1_return
            self.root.quit()
        else:
            if x:
                self.returning = x#returns entry
                self.root.quit()

    def b2_action(self, event=None):#defines action to button 2
        x = "Guess" #returns Guess string name
        self.returning = x
        self.root.quit()

    # remove this function and the call to protocol
    # then the close button will act normally
    def close_mod(self):
        pass

    def time_out(self):
        try: x = self.entry.get()
        except AttributeError: self.returning = None
        else: self.returning = x
        finally: self.root.quit()

    def to_clip(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.msg)

    def mbox(msg, b1='OK', b2='Cancel', frame=True, t=False, entry=False):
        """Create an instance of MessageBox, and get data back from the user.
        msg = string to be displayed
        b1 = text for left button, or a tuple (<text for button>, <to return on press>)
        b2 = text for right button, or a tuple (<text for button>, <to return on press>)
        frame = include a standard outerframe: True or False
        t = time in seconds (int or float) until the msgbox automatically closes
        entry = include an entry widget that will have its contents returned: True or False
        """
        msgbox = MessageBox(msg, b1, b2, frame, t, entry)
        msgbox.root.mainloop()
        # the function pauses here until the mainloop is quit
        msgbox.root.destroy()
        return msgbox.returning