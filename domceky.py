from turtle import exitonclick, forward, left, right
from math import degrees, sqrt, tan 

def domcek(sirka,vyska):
    forward(s) 
    left(90)
    forward(v)
    right (180)
    right(tn)
    forward(e)
    
    



s = int(input('zadaj sirku: '))
v = int(input('zadaj vysku: '))
e = sqrt(s**2 + v**2)
tn = degrees(tan(s/v))
domcek(s,v )

print(str(tn))


exitonclick()