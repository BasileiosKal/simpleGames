#Module with the functions that create the windows with the clues.
#Each function is called when the corresponded button is pressed, and
#creates a separate Window that contains a graphic representetion of
#the clue and a sort text that explains it.
#
#1.The First Clue: The clue is that the pattern is reapeating it self every two rows.
#                  The function, for graphic representation will create a create a matrix
#                  with dots in the place of the numbers and a yellow rectangle around
#                  every two rows of the matrix (without overlapping).
#2.The Second Clue: The clue is that the sum of the numbers in its raw is constant.
#                   The function will create a matrix with dots in the place of the
#                   numbers and lines connecting the dots in the same row.
#3.The Third Clue: The clue is that the sum of the numbers in some specific points of the matrix
#                  (that are repeated every two rows) is constant. Again, the function will create
#                  a matrix with dots in the place of the numbers and lines connecting the dots
#                  that correspond with that points.

from graphics import *

#--------------------------------------------------------------------------------------------------------------------------------------#
##================##
##   First Clue   ##
##================##
def FirstClue():
    #Creating the First Clue window
    ClueWin = GraphWin('Clue',400,300)
    ClueWin.setBackground('black')
    
    #----draw the cels with circles instead of the numbers-----#
    #coordinates for the upper corner of the matrix
    startY = 40
    startX = 20
    LineLen = 240 #length of the vertical lines of the matrix
    step = 40 #distance between the vertical lines
    stepY = LineLen/6 #distance between the horizontal lines
    RectVertices = [] #List that will hold the Points for the rectangle over every two rows of the matrix.
    
    #Horizontal lines
    for ii in range(0,4):
        line = Line(Point(startX+step*ii,startY),Point(startX+step*ii,startY+LineLen))
        line.setFill('white')
        line.draw(ClueWin)
    #Vertical lines
    for kk in range(0,7):
        line2 = Line(Point(startX,startY+kk*(stepY)),Point(startX+3*step,startY+kk*(stepY)))
        line2.setFill('white')
        line2.draw(ClueWin)
    #Displaying the circles (dots) in the cells
    for tt in range(0,6):
        for rr in range(0,3):
            pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+tt*stepY)
            circles = Circle(pt,5)
            circles.setFill('white')
            circles.draw(ClueWin)
            #Appending in the RectVertices the Points of the rectangle
            if tt%2 == 0 and rr == 0:   #the upper left corner of the rectangle
                pt1 = Point(startX+rr*step, startY+tt*stepY)
                RectVertices.append(pt1)
            if tt%2 == 1 and rr == 2:   #the lower right corner of the rectangle
                pt2 = Point(startX+(rr+1)*step, startY+(tt+1)*stepY)
                RectVertices.append(pt2)
        #drawing the rectangle
        #for tt == 1 will make a rectangle around the first two rows
        #for tt == 3 will make one around the next two rows
        #for tt == 5 will make one around the last two rows (the matrix has 6 rows as a whole).
        if tt == 1 or tt == 3 or tt == 5:  
            Rect = Rectangle(RectVertices[0],RectVertices[1])
            Rect.setWidth(3)
            Rect.setOutline('yellow')
            Rect.draw(ClueWin)
            RectVertices=[]

    #----Labels and text----#
    #Title
    Title = Text(Point(ClueWin.getWidth()/2,20),'First Clue')
    Title.setFill('white')
    Title.draw(ClueWin)
    #Clue Explanation
    Explanation3 = Text(Point(ClueWin.getWidth()*(3/4)-10,150),'The pattern is repeated \nevery two rows')
    Explanation3.setFill('white')
    Explanation3.draw(ClueWin)


#--------------------------------------------------------------------------------------------------------------------------------------#
##=================##
##   Secont Clue   ##
##=================##
def SecontClue():
    #Creating the Secont Clue window
    ClueWin = GraphWin('Clue',400,300)
    ClueWin.setBackground('black')
    
    #----draw the cels with circles instead of the numbers-----#
    #coordinates for the upper corner of the matrix
    startY = 40
    startX = 20
    LineLen = 240      #length of the vertical lines of the matrix
    step = 40          #distance between the vertical lines
    stepY = LineLen/6  #distance between the horizontal lines

    #Horizontal lines
    for ii in range(0,4):
        line = Line(Point(startX+step*ii,startY),Point(startX+step*ii,startY+LineLen))
        line.setFill('white')
        line.draw(ClueWin)
    #Vertical lines
    for kk in range(0,7):
        line2 = Line(Point(startX,startY+kk*(stepY)),Point(startX+3*step,startY+kk*(stepY)))
        line2.setFill('white')
        line2.draw(ClueWin)
        #Drawing the lines that connect the dots in the same row
        if kk < 6:
            SolutionLine = Line(Point(startX+10,startY+kk*(stepY)+stepY/2),Point(startX+3*step-10,startY+kk*(stepY)+stepY/2))
            SolutionLine.setFill('yellow')
            SolutionLine.draw(ClueWin)
    #Displaying the circles (dots) in the cells
    for tt in range(0,6):
        for rr in range(0,3):
            pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+tt*stepY)
            circles = Circle(pt,5)
            circles.setFill('white')
            circles.draw(ClueWin)



    #----Labels and text----#
    #Title
    Title = Text(Point(ClueWin.getWidth()/2,20),'Secont Clue')
    Title.setFill('white')
    Title.draw(ClueWin)
    #Clue Explanation
    Explanation3 = Text(Point(ClueWin.getWidth()*(3/4)-10,150),'The sum of the numbers \nin the yellow lines is constant')
    Explanation3.setFill('white')
    Explanation3.draw(ClueWin)



#--------------------------------------------------------------------------------------------------------------------------------------#
##================##
##   Third Clue   ##
##================##
def ThirdClue(Points):
    #Creating the Secont Clue window
    ClueWin = GraphWin('Clue',400,300)
    ClueWin.setBackground('black')
    
    #----draw the cels with circles instead of the numbers-----#
    #coordinates for the upper corner of the matrix
    startY = 40
    startX = 20
    LineLen = 240       #length of the vertical lines of the matrix
    step = 40           #distance between the vertical lines
    stepY = LineLen/6   #distance between the horizontal lines
    RedVertices = []    #List that will hold the Points for the lines that will connect the points of the pattern.
    
    #Horizontal lines
    for ii in range(0,4):
        line = Line(Point(startX+step*ii,startY),Point(startX+step*ii,startY+LineLen))
        line.setFill('white')
        line.draw(ClueWin)
    #Vertical lines
    for kk in range(0,7):
        line2 = Line(Point(startX,startY+kk*(stepY)),Point(startX+3*step,startY+kk*(stepY)))
        line2.setFill('white')
        line2.draw(ClueWin)

    #Displaying the circles in the cels
    for tt in range(0,6):
        for rr in range(0,3):
            pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+tt*stepY)
            circles = Circle(pt,5)
            circles.setFill('white')
            #Appending in the RedVertices List the Points of the lines that will
            #connect the points of the pattern.
            if [tt%2,rr] in Points:
                RedVertices.append(pt)
                circles.setFill('red')    
            circles.draw(ClueWin)

        #Displaying the lines that will connect the points of the pattern.
        if tt == 1 or tt == 3 or tt == 5:
            RedLine1 = Line(RedVertices[0],RedVertices[1])
            RedLine2 = Line(RedVertices[1],RedVertices[2])
            RedLine1.setFill('red')
            RedLine2.setFill('red')
            RedLine1.setWidth(0.5)
            RedLine2.setWidth(0.5)
            RedLine1.draw(ClueWin)
            RedLine2.draw(ClueWin)
            RedVertices=[]


    #----Labels and text----#
    #Title
    Title = Text(Point(ClueWin.getWidth()/2,20),'Third Clue')
    Title.setFill('white')
    Title.draw(ClueWin)
    #Solution Explanation
    Explanation2 = Text(Point(ClueWin.getWidth()*(3/4)-10,150),'The sum of the numbers \nin the red points is constant')
    Explanation2.setFill('white')
    Explanation2.draw(ClueWin)

