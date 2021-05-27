import turtle

colors = ["red","orange","yellow","green","blue","purple"]

tortuga = turtle.Turtle()
len = 100
index = 0

tortuga.speed(0)
def square (len):
    for i in range (4):
        tortuga.forward(len)
        tortuga.right (90)

for i in range (72):            
    tortuga.color(colors[index])    
    square(len)
    tortuga.right (5)
    if ((i%12)==11): 
        index+=1       

tortuga.screen.exitonclick()
tortuga.screen.mainloop()