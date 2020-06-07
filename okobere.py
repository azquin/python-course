from random import randrange



stav = 0 
random = randrange(2, 11)
odpoved = ' '
i = 0


while stav <=21:
    stav = randrange(2, 11)
    i = i + stav
    print('Tvoje skóre je: ' , i)
    if i == 21:
            print('Vyhral si, tovje skóre je : ' , i )
            break
    elif i > 21:
        print('prehral si hahahah') 
        break       
    odpoved = input('povedz či chceš hrat! ')
    if odpoved == 'ano':
            print('hráme')
    elif odpoved != 'ano':
        print('Koniec, tvoje skóre je : ' , i)
        break    

        
    
            


    