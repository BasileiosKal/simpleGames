#Παιχνίδι της κρεμάλας στο οποίο πρέπει να μαντέψετε ονόματα μεθόδων κάποιων βασικών τύπων της Python,
#όπως αυτά επιστρέφονται από τη συνάρτηση dir.
#Η main συνάρτηση.

import random

from wordGuessing import wordGuessing
from RandomWord import RandomWord
from draw import draw
from findLetters import findLetters
from ListToString import ListToString

def main():
    end = False   #Θα γίνει True όταν ο χρήστης δε θέλει να παίξει άλλο.
    WordNumber = 1
    HighScore = 0
    while not end:
        Score = 0
        mistakes = 0
        [SecretWord, ty] = RandomWord()   
        Guesed = ''
      #  print(SecretWord)
        DashStr = len(SecretWord)*'-'       #Την DashStr πρώτα τη μετατρέπω σε λίστα για να την τροποποιήσω εύκολα (μέσω της wordGuesing() που δέχεται list για αυτό τον λόγο)
        DashList = list(DashStr)            #και μετά πάλι σε γραμματοσειρά (μέσω της ListToString()) για να τυπωθεί στην οθόνη και να συγκριθεί με την SecretWord .   
        while mistakes < 5 and DashStr != SecretWord: #Η επανάληψη θα σταματήσει όταν γίνει το 5ο λάθος η όταν βρεθεί η μυστική λέξη (DashStr == SecretWord).
            draw(mistakes, Guesed, WordNumber, Score, HighScore, DashStr)    #Εμφάνιση της κρεμάλας, της βαθμολογίας,των παυλών και των σοστών γραμμάτων.
            #Είσοδος απο τον παίχτη ενώς χαρακτήρα και ανανέωση της DashList,των λαθών και του σκόρ ανάλογα με την είσοδο, όπως αυτά επιστρέφονται απο την wordGuesing().
            [DashList, mistakes, Guesed, Score] = wordGuessing(SecretWord, mistakes, Guesed, DashList, Score)
            DashStr = ListToString(DashList)                                                             
        if mistakes >= 5: #Αν έγιναν πάνω απο 5 λάθη ο παίχτης έχασε.
            draw(mistakes, Guesed, WordNumber, Score, HighScore, DashStr)
            print('Sorry, the word was',SecretWord,"from ", ty)
            HighScore = 0
        else: #Αν έγιναν λιγότερα απο 5 λάθη,για να τελείωσε η επανάληψη, σημαίνει οτι βρέθηκε η λέξη.
            print('Congrats, the word was',SecretWord,"from ", ty)
            HighScore += 1
        WordNumber += 1

        ans = str(input("\nAnother one? (Y/n)"))
        if ans.lower() != 'y' and ans.lower() != 'yes': #Έχω βάλει το .lower() για να δέχεται και τα 'Υ','Yes','YES' κλπ,σαν εισόδους αν ο χρήστης θέλει να συνεχίσει.
            end = True
    
main()
