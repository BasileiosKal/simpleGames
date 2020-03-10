#Function that creates the window that will appear if the
#correct answer is given. The window will contain the message ''CORRECT!!''
#and two buttons, one button that quits the game and one that lets the user to
#play again a new game. The function will return True if the user wants to
#play again and False otherwise. If the wrong answer is given the function will
#draw a message in the main window

from graphics import *
from Buttons import *

def CorrectAnswer(win,name,strAnswer,entry1_X,entry1_Y):
    endGame = False
    if (name == strAnswer) or (str(name.replace(',','')) == str(strAnswer)): #if the answer was correct
        endGame = True
        #----New window----#
        CorrectAnswerWin = GraphWin('Correct',300,150)
        CorrectAnswerWin.setBackground('black')
        #Message to print
        LabelCorrect = Text(Point(150,42),'CORRECT!!')
        LabelCorrect.setSize(28)
        LabelCorrect.setTextColor('red')
        LabelCorrect.draw(CorrectAnswerWin)
        
        #----Buttons----#
        #Length and Position
        #Button to play again
        AgainBt_Xlen = 100
        AgainBt_Ylen = 30
        AgainBt_X = 220
        AgainBt_Y = 100
        #Button to quit the game
        QuitBt_Xlen = 100
        QuitBt_Ylen = 30
        QuitBt_X = 80
        QuitBt_Y = 100
        
        #Display the buttons
        #Button to play again
        buttons(CorrectAnswerWin,AgainBt_X,AgainBt_Y,AgainBt_Xlen,AgainBt_Ylen,'Play Again')
        #Button to quit the game
        buttons(CorrectAnswerWin,QuitBt_X,QuitBt_Y,QuitBt_Xlen,QuitBt_Ylen,'Quit')

        #Checking if a button is pressed
        #The program will wait for the user to press a button
        PressQuit = False
        PressAgain = False
        while not PressQuit or not PressAgain:
            clickPt = CorrectAnswerWin.getMouse()
            PressQuit = pressButton(CorrectAnswerWin,clickPt,QuitBt_X,QuitBt_Y,QuitBt_Xlen,QuitBt_Ylen)
            if PressQuit:
                CorrectAnswerWin.close()
                win.close()               #The main window must be closed regardless but before the function returns something.
                return [False,endGame] 
            PressAgain = pressButton(CorrectAnswerWin,clickPt,AgainBt_X,AgainBt_Y,AgainBt_Xlen,AgainBt_Ylen)
            if PressAgain:
                CorrectAnswerWin.close()
                win.close()
                return [True,endGame]
    else: #if the answer was not correct
        LabelWrong = Text(Point(entry1_X,entry1_Y+40),'Wrong, please try again')
        LabelWrong.setFill('white')
        LabelWrong.draw(win)
        time.sleep(1.4)
        LabelWrong.undraw()
        return [False,endGame]
        

