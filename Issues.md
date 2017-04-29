# Math24 projec

Basically the code I pushed into repo is a combined modification of two projects from Gitub.
 - Calculater https://github.com/prodicus/pyCalc
 - Math24Solver https://github.com/Nate-/Math24

The general layout is from Calculator (most part of the code), where solution comes from Math24solver (the first part, Math24solver class). There are two very different coding styles so far. Some functions/methods are not needed for our project and need to be cleaned. 

## Some issues


 2 (Alla-Completed)- We need to add display of the rule for this game somewhere, so player can know how to play.
 3-(Jun- Completed) We should use all four numbers and each number can be used only once, each number must be followed by an operator. 
	Current code will show succeed if you click "=" and whatever showing on textbox gives you 24.
 4- We need to add Timer
 5- (Alla/Jun -Completed) Not sure how to define that you loose or win current game. 
 7- Instead showing numbers, we may want to show card images. I think it will be cool.
 9- What is the condition that you win the final game? points? It is not implemented.
 10-(Alla-Completed: Will add game instructions in the About-->Help) We can add something in dropdown menu.
 11-Writting test, at least for each function/method.
 12-(Alla-WIP): Manual UI testing. Will document all the tests performed.
 13-(): Include a solution row immediately below were we type in the answer that will display the solution in the event of a loss.
 14-(Alla-Completed): Include an enhancement that prevents users from repeatadly clicking the "solution" button which increases the 
	losses score. 
 15-(Alla-Completed): Include an enhancement that prevents adding to the losses count in the event you click on the "Solution" button when you 
	loose a game round since you already have the loss count goes up by one when you loose.
 16-(Alla-Completed): Include an enhancement that prevents adding to the losses or wins count in the event you click on the "Solution" button
				just to see the system version of the solution.
---------------------------------------------- 
 UNKNOWN (ISSUES THAT ARE NOT CLEAR):
----------------------------------------------
1.Idea is that you don't get success and click new game button or time is up. But it is not implemented yet.
2.Because it is modified from calculator, the original design is single digital for each button. 
	I found sometimes it showed some wired insertion when it handles double digital. 
	
------------------------------------------------------------------------------------
ISSUES PREVIOULSY DECLARED AS AN ISSUE, BUT ARE QUESTIONABLE (POTENTIALY NOT REQUIRED):
------------------------------------------------------------------------------------
The final layout is not an object, just several functions are combined together. 
	I think it will be better that we can reformat it. It will make unit-test much easier.
