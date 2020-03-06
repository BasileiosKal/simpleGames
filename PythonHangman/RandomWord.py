#Συνάρτηση για την παραγωγή της τυχαίας λέξης. Αρχικά θα επιλέγεται ένας τυχαίος αριθμός από το 1 εώς το 6,
#που θα αντιστοιχεί στους τύπους: συμβολοσειρές, ακέραιους, πραγματικούς, λίστες, πλειάδες, λεξικά και σύνολα
#μετά ανάλογα με την παραπάνω επιλογή θα επιλέγει μια τυχαία λέξη απο τις λίστες (dir) του αντίστοιχου τύπου
#και θα επιστρέφει την λέξη(Word) και τον τύπο(typeOf)
import random

def RandomWord():
    def makeList(A):           #Συνάρτηση που επιστρέφει λίστες χωρίς τα αρχικά στοιχεία που αρχίζουν από '_'
        n = 0                  #χρησιμοποιήτε για να φτιάχνει τις λίστες απο όπου θα επιλέγετε η κρυφή λέξη
        while A[n][0]=='_':    #'αφαιρώντας' τα αρχικά στοιχεια που αρχίζουν με '_'(είδα οτι η dir βάζει αυτά τα στοιχεία πάντα στην αρχή) 
            n=n+1
        return A[n+1:]

    c = random.randint(0,6)   #Επιλογή μεταξύ str(c=0),int(c=1),float(c=2),list(c=3),tuples(c=4),dictionarys(c=5),sets(c=6)
    #Σε κάθε περίπτωση, L: η λίστα χωρίς τα στοιχεία που αρχίζουν με '_'
    #                   r: ένας αριθμός μεταξύ 0 και len(L)-1 και L[r]: το τυχαίο στοιχείο της λίστας  
    if c == 0:
        L =makeList(dir(str))                   
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "str"
    elif c == 1:
        L =makeList(dir(int))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "int"
    elif c == 2:
        L =makeList(dir(float))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "float"
    elif c == 3:
        L =makeList(dir(list))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "list"
    elif c == 4:
        L =makeList(dir(()))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "Touples"
    elif c == 5:
        L =makeList(dir({}))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "Dictionarys"
    elif c == 6:
        L =makeList(dir(set))
        r = random.randint(0, len(L)-1)
        Word = L[r]
        typeOf = "set"
    return Word, typeOf
