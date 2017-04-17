import os.path
import string
import re
import sys

class LDR(object):
    """Holds all static functions for leaderboard functionality"""
    
    #Function takes a db txt file path (string), parses all names score, and return a list
    def getLeaderBoard(databasefile):
        leaders = LDR.sortLeaderBoard(databasefile)
        print('LeaderBoard')
        print('Rank','Name','Score')
        rank = 1
        topten =0;    
        for name, score in leaders:
            if topten<=9:
                print(rank,name,score)
                rank=rank+1
                topten=topten +1
            else:
                break       
    #Function that sorts leaderboard database file
    def sortLeaderBoard(databasefile):
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
            LeaderBoardDataBaseFile = open(databasefile,"w")
            LeaderBoardDataBaseFile.close()
        leaders = sorted(LeaderBoardParseList, key = lambda lead: lead[1], reverse = True) #sorts list of tuples
        for CurrentTuple in leaders:
                
            LDR.appendToLeaderBoard(databasefile, CurrentTuple[0], CurrentTuple[1])
        return leaders     
    #Function takes a db text file path (string), name and score, overwrite file
    def overWriteLeaderBoard(databasefile, name, score):
        LeaderBoardDataBaseFile = open(databasefile, "w")
        try:
            leader = name+','+str(score)+'\n'
            LeaderBoardDataBaseFile.write(leader)
        finally:
            LeaderBoardDataBaseFile.close()
           
    #Append Leader name and score to leaderboard
    def appendToLeaderBoard(databasefile, name, score):
        LeaderBoardDataBaseFile = open(databasefile, "a")
        try:
            leader = name+','+str(score)+'\n'
            LeaderBoardDataBaseFile.write(leader)
        finally:
            LeaderBoardDataBaseFile.close()
    #Check if database is empty
    def checkIfDataBaseFileIsEmpty(pathstring):
        LeaderBoardDataBaseFile = open(pathstring)
        if  LeaderBoardDataBaseFile.readline() == " ":
            LeaderBoardDataBaseFile.close()
            return True
        else:
            LeaderBoardDataBaseFile.close()
            return False
    #Check if database txt file exists
    def checkIfDataBaseFileExist(pathstring):
        if os.path.isfile(pathstring):
           return True
        else:
           return False
    #Check if databse is full(10 Leaders)
    def checkIfDataBaseFileIsFull(pathstring):
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
            