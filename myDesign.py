import turtle#brings in turtle library
from myFunctions import*#brings in custom functions
turtle.colormode(255)
turtle.bgcolor("Black")
bob=turtle.Turtle()#sets bob as a variable to represent turtle
bob.speed(11)#speeds up the drawing process
jump(bob,0,0)#custom function, moves to specific coordinate without making a marking

for times in range(360):#repeats the below code 98 times
     bob.right(11)
     bob.color(255,0,0)
     bob.circle(1*times+6)
     bob.color(0,255,0)
     bob.circle(2*times+5)
     bob.color(0,0,255)
     bob.circle(3*times+4)
     bob.color(255,255,0)
     bob.circle(4*times+3)
     bob.color(255,0,255)
     bob.circle(5*times+2)
     bob.color(0,255,255)
     bob.circle(6*times+1)
     
