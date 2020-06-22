#Napiš program, který simuluje tuto hru:

#První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6),
# dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu.
 # Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. 
 # (V případě shody vyhraje ten, kdo házel dřív.)

#Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.


poradie = 0 
lol = 0
vitaz = ''
while poradie != 4:
    from random import randrange


    hod = 0
    j= 0
    i = 0
    y_a = "prvyhrac","druhyhrac","tretihrac","stvrtyhrac" 
    


    while j != 6:
        j = randrange(1,7) 
        print(f"""{y_a[0 + poradie]} hadze cislo: {j} """)
        hod = hod + 1
    if hod > lol:
        vitaz = y_a[0 + poradie]    
    if hod > lol:
        lol = hod
    print(f"""{y_a[0 + poradie]} hodil cislo: {j} na {hod}.pokus \n """)
    poradie = poradie + 1


print(f""" {vitaz} je vitaz so {lol} hodmi""")




