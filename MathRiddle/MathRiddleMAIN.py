##################################################################################################################
#a game that you must find the missing numbers in a 6x3 matrix by discovering the hidden pattern behind          #
#the numbers in the matrix that are known. The pattern is partially randomly generated, mining that will follow  #
#a set of predetermined rules but will also have random generated elements. Of corse the set of predetermined    #
#rules is enough to make the riddle always have a solution.                                                      #
##################################################################################################################

import random
from graphics import *
from GUI import *

#Returns a list with all the integers that sum to N
def NumbersThatSumTo(N):
    L = []
    for ii in range(1,N+1):
        for kk in range(1,N-ii+1):
            ll = N-ii-kk
            L.append([ii,kk,ll])
    return(L)


#Function that returns a list with the numbers that will
#belong in the pattern. Given the number c and the position
#of the numbers that will have sum c in the matrix the function,
#from the list's of all 3 integers that sum to N will keep
#the ones that, if put in a 2x3 matrix will create the pattern,
#meaning that the numbers with the indexes in the list Points
#will have sum c.
def creatingPatern(X,Y,Points,c):
    L = []
    for xx in X:
        for yy in Y:
            xy = [xx,yy]
            if xy [Points[0][0]][Points[0][1]]+xy[Points[1][0]][Points[1][1]]+xy[Points[2][0]][Points[2][1]] == c:
                L.append([xx,yy])
    return(L)

#Function that returns a list with random points for the pattern.
#In the indexes specified by that points the sum will be constant.
def RandomPoints():
    setOfPoints = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]
    Points = random.sample(setOfPoints,3)
    return(Points)

##=================================================================##
##                        main function                            ##
##=================================================================##
def main():
    playAgain = True
    while playAgain:
        LaunchAgain = True
        while LaunchAgain:
            matrix = []
            Points = RandomPoints()
            flag = 0
            sumOfLines = random.randrange(10,30)      #the sum of numbers in the rows.
            SumInPatern = random.randrange(sumOfLines+5,sumOfLines+15)    #the sum of numbers in the pattern.
            for ii in range(3):
                P1 = []              #list for the numbers that satisfy the pattern
                while len(P1) == 0 and flag<100:   #waiting for a non-empty pattern
                    L1 = NumbersThatSumTo(sumOfLines)  #lists of numbers with constant sum to go to each row
                    L2 = NumbersThatSumTo(sumOfLines)  #there’s two because i wanted to live the possibility each row to have a different sum
                    P1 = creatingPatern(L1, L2,Points,SumInPatern)
                    flag += 1
                if flag >= 100:
                    break
                choise = random.randrange(len(P1))
                matrix.append(P1[choise][0])   #appending the numbers to the matrix two rows at the time
                matrix.append(P1[choise][1])
                if ii == 2:
                    LaunchAgain = False
            if flag >= 100:
                break
            else:
                LaunchAgain = False
            #greating the main GUI
            playAgain = drawGUI(matrix,Points,sumOfLines,SumInPatern) #Will be True if the user want to play again.

main()        

