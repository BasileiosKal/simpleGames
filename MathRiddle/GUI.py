#Function for displaying the User Interphase. The graphics are
#created using the graphics.py module developed by John Zelle
#for use with his Python Programming book.
#The GUI main window will contain:
#
#   1. The actual riddle (the matrix with the known
#      numbers and the '?' in the place of the secret ones).
#   2. An entry obj for the User to type his solution and a corresponding label.
#   3. Buttons for Clues and the Solution, an Exit button and a
#      Enter button. The first two buttons will open different windows
#      to display clues or the solution. The enter button will open a different window
#      that asks the user if he wants to play again or quit the game, only if the
#      answer given is correct.


from graphics import *                  #the graphics.py module developed by John Zelle.
from Buttons import *                   #module for the creation of buttons and checking if the button is pressed.
from SolutionWindows import *           #module for the creation of the window with the solution.
from ClueWindows import *               #module for the creation of the windows with the clues.
from CorrectAnswerWindow import *       #module for the creation of the window that will appear if the answer is correct.

def drawGUI(NumberMatrix,Points,sumInRows,SumInPatern):
    Answer = NumberMatrix[5]
    strAnswer = str(Answer[0])+str(Answer[1])+str(Answer[2])

    #Creating the main window
    win = GraphWin('Riddle',400,400)
    win.setBackground('black')
    
    ##========================================##
    ##    draw the cells with the numbers     ##
    ##========================================##
    #coordinates for the upper corner of the matrix
    startY = 40  
    startX = 100
    LineLen = 240  #length of the vertical lines of the matrix
    step = 40 #distance between the vertical lines
    stepY = LineLen/6  #distance between the horizontal lines
    #Vertical lines
    for ii in range(0,4):
        line = Line(Point(startX+step*ii,startY),Point(startX+step*ii,startY+LineLen))
        line.setFill('white')
        line.draw(win)
    #Horizontal lines
    for kk in range(0,7):
        line2 = Line(Point(startX,startY+kk*(stepY)),Point(startX+3*step,startY+kk*(stepY)))
        line2.setFill('white')
        line2.draw(win)
    #Displaying the numbers of the matrix in the cells
    for tt in range(0,5):
        for rr in range(0,3):
            pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+tt*stepY)
            numperToPrint = NumberMatrix[tt][rr]
            label = Text(pt,str(numperToPrint))
            label.setFill('white')
            label.draw(win)
    #Displaying the '?' in the 3 last cells
    for rr in range(0,3):
        pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+5*stepY)
        label = Text(pt,'?')
        label.setFill('white')
        label.draw(win)

    ##===========================##    
    ##   Entry for the answer    ##
    ##===========================##
    #Entry position parameters
    entry1_X = startX+46
    entry1_Y = startY+LineLen+40
    #Entry obj
    entry1 = Entry(Point(entry1_X,entry1_Y),10)
    entry1.draw(win)
    #Text label for the Entry obj
    EntryLabel = Text(Point(entry1_X-90,entry1_Y),'Solution:')
    EntryLabel.setFill('white')
    EntryLabel.draw(win)
    
    ##=================##
    ##     buttons     ##
    ##=================##
    #---Position Parameters---#
    #for the Enter button
    EnterBt_X = entry1_X+80  #X button coordinate
    EnterBt_Y = entry1_Y-1   #Y button coordinate
    EnterBt_Xlen = 50        #Horizontal button length
    EnterBt_Ylen = 22        #Vertical button length
    #for the First Clue button
    Clue1Bt_Xlen = 70
    Clue1Bt_Ylen = 22
    Clue1Bt_X = startX+3*step+100
    Clue1Bt_Y = startY+Clue1Bt_Ylen/2
    #for the Secont Clue button
    Clue2Bt_Xlen = 70
    Clue2Bt_Ylen = 22
    Clue2Bt_X = startX+3*step+100
    Clue2Bt_Y = Clue1Bt_Y+Clue2Bt_Ylen/2+20
    #for the Third Clue button
    Clue3Bt_Xlen = 70
    Clue3Bt_Ylen = 22
    Clue3Bt_X = startX+3*step+100
    Clue3Bt_Y = Clue2Bt_Y+Clue2Bt_Ylen/2+20
    #for the Solution button
    SolutionBt_Xlen = 70
    SolutionBt_Ylen = 22
    SolutionBt_X = startX+3*step+100
    SolutionBt_Y = Clue3Bt_Y + Clue3Bt_Ylen/2 + 20
    #for the Exit button
    ExitBt_Xlen = 70
    ExitBt_Ylen = 22
    ExitBt_X = startX+3*step+100
    ExitBt_Y = SolutionBt_Y + SolutionBt_Ylen/2 + 20

    #---Creating the buttons---#
    #Enter button
    buttons(win,EnterBt_X,EnterBt_Y,EnterBt_Xlen,EnterBt_Ylen,'Enter')
    #Clue 1 button
    buttons(win,Clue1Bt_X,Clue1Bt_Y,Clue1Bt_Xlen,Clue1Bt_Ylen,'Clue 1')
    #Clue 2 button
    buttons(win,Clue2Bt_X,Clue2Bt_Y,Clue2Bt_Xlen,Clue2Bt_Ylen,'Clue 2')
    #Clue 3 button
    buttons(win,Clue3Bt_X,Clue3Bt_Y,Clue3Bt_Xlen,Clue3Bt_Ylen,'Clue 3')
    #Solution button
    buttons(win,SolutionBt_X,SolutionBt_Y,SolutionBt_Xlen,SolutionBt_Ylen,'Solution')
    #Exit button
    buttons(win,ExitBt_X,ExitBt_Y,ExitBt_Xlen,ExitBt_Ylen,'Exit')

    #---waiting for the user to press a button and calling the appropriate function---#
    PressEnter = False
    PressExit = False
    PressSolution = False
    endGame = False
    PlayAgain = False
    
    #the window will close (and the while loop will end)
    #only if the user press exit or if he finds the correct answer
    while not PressExit and not endGame:
        
        clickPt = win.getMouse() #waiting for a click
        
        #Checking the answer if the enter button is pressed
        PressEnter = pressButton(win,clickPt,EnterBt_X,EnterBt_Y,EnterBt_Xlen,EnterBt_Ylen)
        if PressEnter:
            name = entry1.getText() #reading the answer from the entry obj
            [PlayAgain,endGame] = CorrectAnswer(win,name,strAnswer,entry1_X,entry1_Y) #Displaying the CorrectAnswer window if the
                                                                                      #enter button is pressed and the answer was correct.

        #Checking if the Solution button is pressed.
        PressSolution = pressButton(win,clickPt,SolutionBt_X,SolutionBt_Y,SolutionBt_Xlen,SolutionBt_Ylen)
        if PressSolution:
            SolutionWindow(Points,Answer,sumInRows,SumInPatern) #Displaying a window with the solution if the Solution buton is pressed

        #Checking if the First Clue button is pressed.
        PressFirstClue = pressButton(win,clickPt,Clue1Bt_X,Clue1Bt_Y,Clue1Bt_Xlen,Clue1Bt_Ylen)
        if PressFirstClue: 
            FirstClue() #Displaying a window with the First Clue if the button is pressed

        #Checking if the Second Clue button is pressed.
        PressSecondClue = pressButton(win,clickPt,Clue2Bt_X,Clue2Bt_Y,Clue2Bt_Xlen,Clue2Bt_Ylen)
        if PressSecondClue:
            SecontClue() #Displaying a window with the Second Clue if the button is pressed

        #Checking if the Third Clue button is pressed.
        PressThirdClue = pressButton(win,clickPt,Clue3Bt_X,Clue3Bt_Y,Clue3Bt_Xlen,Clue3Bt_Ylen)
        if PressThirdClue:
            ThirdClue(Points) #Displaying a window with the Third Clue if the button is pressed

        #Checking if the Exit button is pressed.
        PressExit = pressButton(win,clickPt,ExitBt_X,ExitBt_Y,ExitBt_Xlen,ExitBt_Ylen)
        if PressExit:
            PlayAgain = False
            win.close() 

    return PlayAgain
