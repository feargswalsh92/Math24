# Math24 projec

Basically the code I pushed into repo is a combined modification of two projects from Gitub.
 - Calculater https://github.com/prodicus/pyCalc
 - Math24Solver https://github.com/Nate-/Math24

The general layout is from Calculator (most part of the code), where solution comes from Math24solver (the first part, Math24solver class). There are two very different coding styles so far. Some functions/methods are not needed for our project and need to be cleaned. 

## Some issues

 - The final layout is not an object, just several functions are combined together. I think it will be better that we can reformat it. It will make unit-test much easier.
 - We need to add display of the rule for this game somewhere, so player can know how to play.
 - We should use all four numbers and each number can be used only once, each number must be followed by an operator. Current code will show succeed if you click "=" and whatever showing on textbox gives you 24.
 - We need to add Timer
 - Not sure how to define that you lose current game. Idea is that you don't get success and click new game button or time is up. But it is not implemented yet.
 - Winning current game is also not defined. Idea is that you win current game, if you get success display and you will automatically move to next game. It is not implemented yet.
 - Instead showing numbers, we may want to show card images. I think it will be cool.
 - Because it is modified from calculator, the original design is single digital for each button. I found sometimes it showed some wired insertion when it handles double digital. 
 - What is the condition that you win the final game? points? It is not implemented.
 - We can add something in dropdown menu.
 - Writting test, at least for each function/method.
