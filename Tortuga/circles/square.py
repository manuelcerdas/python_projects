import turtle

colors = ["red","orange","yellow","green","blue","purple"]

tortuga = turtle.Turtle()
len = 100
index = 0

#tortuga.speed(0)
tortuga.penup()
tortuga.goto (0,0)
tortuga.pendown()
tortuga.circle (len)
tortuga.penup()
tortuga.forward (len)
tortuga.pendown()
tortuga.circle(len)
tortuga.penup()
tortuga.goto (0,0)


#for i in range (72):            
#    tortuga.color(colors[index])    
#    square(len)
#    tortuga.right (5)
#    if ((i%12)==11): 
#        index+=1       

tortuga.screen.exitonclick()
tortuga.screen.mainloop()