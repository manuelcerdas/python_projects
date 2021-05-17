import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Using Conways "Game of Life rules" determine the value of all the cells in matrix m
# and return them in a new matrix
def matrixLife(m):
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
    return result


# initialize the matrix
# 1 is on, 0 is off
x = np.array([[0,0,1],[1,1,0],[0,1,0]])
y = matrixLife(x)
# ammount of steps we are going to run

#plt.imshow(x, interpolation="nearest")
#plt.show()
print("")
print(x)
print("")
print(y)