#1-D piškvorky se hrají na řádku s dvaceti políčky. Hráči střídavě přidávají kolečka (`o`) a křížky (`x`), třeba:
#1. kolo: -------x------------
#2. kolo: -------x--o---------
#3. kolo: -------xx-o---------
#4. kolo: -------xxoo---------
#5. kolo: ------xxxoo---------
#Hráč, která dá tři své symboly vedle sebe, vyhrál.
#Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

#"x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
#"o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
#"!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
#"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
#Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole
#  (t.j. řetězec) s daným symbolem umístěným na danou pozici.

#Hlavička funkce by tedy měla vypadat nějak takhle:

#def tah(pole, cislo_policka, symbol):  
 #   "Vrátí herní pole s daným symbolem umístěným na danou pozici"
#    ...
#Můžeš využít nějakou funkci, kterou jsme napsaly už na sraze?

velkostpola = input('zadajte velkost pola: ')
hraci = input('Meno hraca 1 ?: '), input('Meno hraca 2 ?: ')
symbol = input('symbol hraca 1 ?: '), input('symbol hraca 2 ?: ')
hrac1 = symbol[0] + symbol[0] + symbol[0]   ##priradi symbol hracovi x
hrac2 = symbol[1] + symbol[1] + symbol[1]   # o
symbolpola = input('zadajte symbol pola: ')
pole = symbolpola
cislo_policka = 0
for n in range(int(velkostpola) - 1 ):
    pole = pole + symbolpola
 

n = 0
i = 0
j = 0 
f = 0
k = 0
premenna = 0


#vyhodnotenie stavu hry funkcia
def vyhodnot(retazec,symbol):
    if hrac1 in pole:       #vyhra hrac 1 vrati
        return symbol[0]
    if hrac2 in pole:       #vyhra hrac 2' vrati 
        return symbol[1]    
    if symbolpola in pole:            #pokracuje sa dalej vrati
        return 'hra este neskoncila'
    else:                   #remiza vrati
        return 'remiza'                
cislo_policka = 0

#tah hraca funkcia
def tah(pole, cislo_policka, symbol):
    if pole[cislo_policka] != symbolpola:
        print('Zadali ste obsadenu poziciu: ')   
    if pole[cislo_policka] == symbolpola:
        return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]          
   

      


for i in range(len(pole)):
    if premenna != 0:
        premenna = 0 


    cislo_policka = (input(hraci[premenna] + ' zadajte poziciu: '))
    cislo_policka = cislo_policka.lstrip()
    cislo_policka = cislo_policka.rstrip()
    cislo_policka = int(cislo_policka)

    
    
   

    pole = tah(pole,cislo_policka,symbol[premenna])
    print(pole)
    vyhodnot(pole,hrac1) 
    if vyhodnot(pole,hrac1) == symbol[0]:
        print('sdhasdsa')
     
    
    premenna = premenna + 1
    
    
    cislo_policka = (input(hraci[premenna] + ', zadajte poziciu: ')) 
    cislo_policka = cislo_policka.lstrip()
    cislo_policka = cislo_policka.rstrip()
    cislo_policka = int(cislo_policka)
    pole = tah(pole,cislo_policka,symbol[premenna])
    print(pole)
    vyhodnot(pole,hrac2)
    if vyhodnot(pole,hrac2) == symbol[1]:
        print('sdhasdsa')
     
     
   

 




        