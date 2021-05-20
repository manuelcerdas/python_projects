import turtle

colors = ["red","green","blue","yellow","orange","black"]

len = 100
colorIndex = 0

turtle.speed(0)
def square (len):
    for i in range (4):
        turtle.forward(len)
        turtle.right (90)

for i in range (72):    
    turtle.color(colors[i % 6])
    square(len)
    turtle.right (5)

input()