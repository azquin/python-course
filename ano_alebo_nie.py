
#Změň funkci ano_nebo_ne tak, aby se místo ano se dalo použít i a, místo ne i n
#  a aby se nebral ohled na velikost písmen a mezery před/za odpovědí.
#Textům jako možná nebo no tak určitě by počítač dál neměl rozumět.

zadaj = '0'

def ano_alebo_nie(rozhodnutie):
   zadaj = (input('rozhodnit sa ci ano ci nie: ')).upper()
   zadaj = zadaj.lstrip()
   zadaj = zadaj.rstrip()
   if zadaj[0] == 'A':
       return zadaj
   elif zadaj[0] == 'N':
       return zadaj    
   else:
       print('napisal si kokotinu zatial okej ?')  
     

ano_alebo_nie(zadaj)

 



