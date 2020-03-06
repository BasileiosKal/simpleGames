#Συνάρτηση που θα ζητάει από το χρήστη να δώσει ένα χαρακτήρα, θα ελέγχει την εγκυρότητα τής εισόδου και αν είναι έγκυρη
#και η μυστική λέξη  έχει αυτό το χαρακτήρα θα αντικαθιστά τις παύλες στην αντίστοιχη θέση στην λίστα DashList με τον χαρακτήρα αυτόν,
#αλλιώς θα αυξάνει τα λάθη κατά 1. Αν η είσοδος δεν ήταν έγκυρη ζητάει από το χρήστη να ξαναδώσει χαρακτήρα μέχρι να δοθεί ένας έγκυρος.
    #Word: η μυστική λέξη.
    #mistakes: Ο αριθμός των λάθος μαντεψιών.
    #guesses: μια συμβολοσειρά με τα γράμματα που έχουν μαντευτεί.
    #DashList: μια λίστα με στοιχεία παύλες στις θέσεις που αντιστοιχούν στα γράμματα που δεν έχουν μαντευτεί σωστά
    #          και τα γράμματα, που έχουν μαντευτεί σωστά, στις αντίστοιχες με την Word θέσεις.
    #Score: το σκόρ.

from findLetters import findLetters

def wordGuessing(Word, mistakes, guesses, DashList, Score):
    #Λίστα με τους επιτρεπτούς χαρακτήρες εισόδου.
    Letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","_"]
    flag = True                                 #Το flag γίνεται False μόνο όταν ο χρήστης δώσει έγκυρη είσοδο.
    while flag:
        Guess = str(input("Guess:"))                        #Ο χαρακτήρας (και η Word αργότερα) γίνεται πεζός, έτσι το πρόγραμμα
        Guess = Guess.lower()                               #δέχεται και τα κεφαλαία γράμματα ως σωστές απαντήσεις.
        if (Guess in Letters) and (Guess not in guesses):   
            if Guess in Word.lower():              
                Score += 1
                pos = findLetters(Word,Guess)              #pos: λίστα με όλες τις θέσεις του χαρακτήρα που έδωσε ο χρήστης, στη μυστική λέξη. 
                for i in pos:
                    DashList[i] = Guess                     #Αντικατάσταση των '-' στήν DashList με το σωστό χαρακτήρα στις αντίστοιχες με την Word θέσεις.
            else:
                mistakes += 1                            
            flag = False                 #Αφού δόθηκε έγκυρος χαρακτήρας το flag γίνεται False για να σταματήσει η επανάληψη.
            guesses = guesses + Guess 
        elif len(Guess)>1:                                  #Περιπτώσεις μη έγκυρων εισόδων και εμφάνιση κατάλληλων μηνυμάτων.
            print('Enter a single letter') 
        elif Guess in guesses and Guess != '': #Το (and Guess != '') υπάρχει για να μήν εμφανίζει 'Already guessed:' αν πατηθεί σκέτο Enter.
            print('Already guessed: ',Guess) 
        else:
            print('Not a valid guess: ', Guess)
    return DashList, mistakes, guesses, Score
