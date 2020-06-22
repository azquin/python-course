#Změň program Kámen, Nůžky, Papír tak, aby opakoval hru dokud uživatel nezadá konec.
from random import randrange

kamen = 0
papier = 1
noznice = 2
stav = 'hh'

print('0 = kamen')
print('1 = papier')
print('2 = noznice')

while stav != 'konec':
    kristian = randrange(0,3)
    matej = randrange(0,3)
    print('Kristian ma: ' + str(kristian))
    print('Matej ma: ' + str(matej))
    if kristian == matej:
        print('remiza')
    if kristian == 0 and matej == 1:
        print('matej vyhral')
    if kristian == 0 and matej == 2:
        print('Kristian vyhral')
    if kristian == 1 and matej == 2:
        print('matej vyhral')
    if matej == 0 and kristian == 1:
        print('kristian vyhral')
    if matej == 0 and kristian == 2:
        print('matej vyhral')
    if matej == 1 and kristian == 2:
        print('kristian vyhral')
    stav = input('AK chces aby hral skoncila zadaj konec: ' )    

    



    
          




