#Function for displaying a window with the solution to the riddle.The window will contain a matrix
#with points of either red or blue instead of numbers and lines that will connect the ones with the same color,
#that have a constant sum, as a graphical representation of the solution. Also, the window will have text that
#will explain the solution and the correct numbers that the user had to find.

from graphics import *

def SolutionWindow(Points,Answer,sumOfLines,SumInPatern):
    #Creating the Solution window
    SolutionWin = GraphWin('solution',400,300)
    SolutionWin.setBackground('black')
    
    #----draw the cels with circles instead of the numbers-----#
    #coordinates for the upper corner of the matrix
    startY = 40
    startX = 20 
    LineLen = 240       #length of the vertical lines of the matrix
    step = 40           #distance between the vertical lines
    stepY = LineLen/6   #distance between the horizontal lines
    RedVertices = []    #List that will hold the Points for the lines that will connect the red points with the constant sum.
    BlueVertices = []   #List that will hold the Points for the lines that will connect the blue points with the constant sum.
    
    #Horizontal lines
    for ii in range(0,4):
        line = Line(Point(startX+step*ii,startY),Point(startX+step*ii,startY+LineLen))
        line.setFill('white')
        line.draw(SolutionWin)
    #Vertical lines
    for kk in range(0,7):
        line2 = Line(Point(startX,startY+kk*(stepY)),Point(startX+3*step,startY+kk*(stepY)))
        line2.setFill('white')
        line2.draw(SolutionWin)

    #Displaying the circles in the cels
    for tt in range(0,6):
        for rr in range(0,3):
            pt = Point(startX+rr*step+(step/2), startY+(stepY/2)+tt*stepY)
            circles = Circle(pt,5)
            #Setting the color and appending in the RedVertices the red Points with the constant sum.
            if [tt%2,rr] in Points:
                RedVertices.append(pt)
                circles.setFill('red')
            #Setting the color and appending in the BlueVertices the blue Points with the constant sum.
            else:
                BlueVertices.append(pt)
                circles.setFill('blue')
            circles.draw(SolutionWin)

        #Drawing the connect the points with the constant sum
        #for tt == 1 will make the lines to connect the points in the first two rows
        #for tt == 3 will make the lines to connect the points in the next two rows
        #for tt == 5 wwill make the lines to connect the points in the last two rows (the matrix has 6 rows as a whole).
        if tt == 1 or tt == 3 or tt == 5:
            #For the red points with the constant sum.
            RedLine1 = Line(RedVertices[0],RedVertices[1])
            RedLine2 = Line(RedVertices[1],RedVertices[2])
            RedLine1.setFill('red')
            RedLine2.setFill('red')
            RedLine1.setWidth(0.5)
            RedLine2.setWidth(0.5)
            RedLine1.draw(SolutionWin)
            RedLine2.draw(SolutionWin)
            RedVertices=[]
            
            #For the blue points with the constant sum.
            BlueLine1 = Line(BlueVertices[0],BlueVertices[1])
            BlueLine2 = Line(BlueVertices[1],BlueVertices[2])
            BlueLine1.setFill('cyan')
            BlueLine2.setFill('cyan')
            BlueLine1.setWidth(0.5)
            BlueLine2.setWidth(0.5)
            BlueLine1.draw(SolutionWin)
            BlueLine2.draw(SolutionWin)
            BlueVertices = []


    #----Labels and text----#
    #Title
    strTitle = str(Answer)
    Title = Text(Point(SolutionWin.getWidth()/2,20),'Solution: '+strTitle[1:len(strTitle)-1])
    Title.setFill('white')
    Title.draw(SolutionWin)
    #Solution Explanation
    #Explanation 1
    Explanation1 = Text(Point(SolutionWin.getWidth()*(3/4)-10,80),'1. The sum of the numbers \nin the red points is: '+str(SumInPatern))
    Explanation1.setFill('white')
    Explanation1.draw(SolutionWin)
    #Explanation 2
    Explanation2 = Text(Point(SolutionWin.getWidth()*(3/4)-10,140),'2. The sum of the numbers \nin the blue points is: '+str(2*sumOfLines-SumInPatern))
    Explanation2.setFill('white')
    Explanation2.draw(SolutionWin)
    #Explanation 3
    Explanation3 = Text(Point(SolutionWin.getWidth()*(3/4)-10,200),"3. The sum of the numbers \n in it's row is: "+str(sumOfLines))
    Explanation3.setFill('white')
    Explanation3.draw(SolutionWin)


