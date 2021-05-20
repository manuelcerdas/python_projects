import turtle

sides = 0

while sides <= 0:
    sides = int(input("How many sides should your polygon sides:"))    
    if (sides <= 0):
        print ("Please type a positive integer number")

angle = 360 / sides

len = 425 / sides

for i in range(sides):
    turtle.forward (len)
    turtle.right (angle)

input()        