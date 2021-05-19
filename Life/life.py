import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Using Conways "Game of Life rules" determine the value of all the cells in matrix m
# and return them in a new matrix
def update(frameNum,m,img):
    # get the matrix size
    rows = m.shape[0]
    columns = m.shape[1]
    result = np.zeros((rows,columns))

    for row in range(0,rows):        
        # using toroidal border conditions
        previousRow = (row - 1) % rows
        nextRow = (row + 1) % rows
                
        for column in range(0,columns):            
            # using toroidal border conditions
            previousColumn = (column - 1) % columns
            nextColumn = (column + 1) % columns

            # since 1 is on and 0 is off
            # adding the neighbors will tell us how many neighbors are on 
            neighborsOn = int(m[previousRow,previousColumn] + m[row,previousColumn] + m[nextRow,previousColumn])
            neighborsOn += int(m[previousRow,column] + m[nextRow,column])
            neighborsOn += int(m[previousRow,nextColumn] + m[row,nextColumn] + m[nextRow,nextColumn])                

            # apply game of life rules to see the value of the cell in the next step
            # since the result matrix is full with ceros, we only have to consider the 
            # cases where the cell turns on

            if (m[row,column] > 0) :
                if ((neighborsOn == 2) or (neighborsOn == 3)):            
                    result[row,column] = 1               
            else: 
                if (neighborsOn == 3):
                    result[row,column] = 1   
            
    img.set_data(result)
    m[:] = result[:]    
    return

#Array size
print ("We are using a square array")
size=input("Please type the size of the array (reccommended 100): ")
size = int(size)


size = 100

# initialize the matrix with
# 1 is on, 0 is off
m = np.random.choice([0,1],size*size,p=[0.2,0.8]).reshape(size,size)

#set up the animation
fig, ax = plt.subplots()
img = ax.imshow(m, interpolation="nearest")
ani = animation.FuncAnimation(fig,update,fargs=(m,img),frames=100,interval=50)
plt.show()



