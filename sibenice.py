from random import randrange


#potialto budu prikazy na import

#priestor pre globalne premenne 
slova = "vino","ulica","streda" #Počítač náhodně zvolí slovo (zatím třeba ze tří možností). 
premenna = randrange(0,3) 
retazec = slova[premenna]
nahrada = ""
i = 0
medzera = " "
zlytah = 0 
pismeno = ""
k = 0 

#priestor pre funkcie
def tah(retazec, cislo_policka, symbol):
    return retazec[:slova[premenna].index(pismeno) * 2 + 1] + pismeno + retazec[slova[premenna].index(pismeno) * 2 + 2:]  





#priestor pre programy
#Nastav výchozí stav: řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
for i in range(int(len(slova[premenna]))):
    nahrada = nahrada + '_' + medzera
nahrada = medzera + nahrada  

print(nahrada)
print(f"""hra sa zacina:  """)
for k in range(20):
    pismeno = input('Zadajte pismeno: ')

    if pismeno in retazec:
        nahrada = tah(nahrada,slova[premenna].index(pismeno),pismeno)
    elif pismeno not in retazec:
        zlytah = zlytah + 1 
        print(pismeno + ' sa nenechadza v hladanom slove')   


    print(nahrada)
    if '_' not in nahrada:
        print(f""" gratulujem vyhrali ste ste s poctom chybnych pokusov: {zlytah} """)
        break
