#Module for the drawing of a button and a function to check if the button is pressed.
#The graphics module by John Zelle, dosen't it self contain a function for
#the displaying of buttons with or without animation. The function here creates a
#button as a Rectangle with a Text obj inside (in the same position). 

from graphics import *

#creates the "button" as a rectangle, with X and Y the center of the rectangle
#and lenX, lenY its dimensions
def buttons(win,X,Y,lenX,lenY,setText):
    rectangle = Rectangle(Point(X-(lenX/2),Y+(lenY/2)),Point(X+(lenX/2),Y-(lenY/2)))
    rectangle.setFill('blue')
    text = Text(Point(X,Y),setText)
    text.setFill('white')
    rectangle.draw(win)
    text.draw(win)

#checks if the user clicked inside the rectangle of the button and
#returns True or False.
def pressButton(win,clickPt,ButtonX,ButtonY,BtLenX,BtLenY):
    clickX = clickPt.getX()
    clickY = clickPt.getY()
    pressed = False
    if (abs(clickX-ButtonX)) < BtLenX/2:
        if (abs(clickY-ButtonY)) < BtLenY/2:
            pressed = True
    return(pressed)

