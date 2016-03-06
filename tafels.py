from random import randint
for i in range(1, 11):
    print ('Som '+str(i)) 
    a = randint(0,10)
    b = randint(0,10)
    antwoord = input('Wat is '+str(a)+' x '+str(b)+'? ')
    goede_antwoord = a*b
    if int(antwoord) == goede_antwoord:
        print('Dat is goed!')
    else:
        print('Sorry, dat is niet goed. Het goede antwoord is '+str(goede_antwoord))

