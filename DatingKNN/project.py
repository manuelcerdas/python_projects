import matplotlib.pyplot as plt
import numpy as np
import classifier as cl
import normalizer as norm
import matplotlib
import matplotlib.pyplot as plt

#Read the training data json
filename = 'data/datingTestSet.txt'

#Read the file as an array of text lines
with open (filename) as f:
    data = f.readlines()

#read the first line of the data and make it an array
firstLine = data[0].strip()

#see how many numeric columns the array has (only the last column is string).  The colums are separated by tabs
gapCount = firstLine.count("\t")

#Adding rows to numpy arrays is very difficult
#In this case since we know the size of the array
#We can initialize the array with zeros
numRows = len(data)
datingData = np.zeros((numRows,gapCount))
labels =  []
#labelsClass stores the labels as int
labelsClass = []
index = 0

for line in data:
    line = line.strip()
    splitLine = line.split("\t");

    #split the line into numeric data and label
    lineData = splitLine[0:gapCount]
    #the last column is the label
    label = splitLine[-1]    
    
    #copy the line to the corresponding line in the array
    datingData[index:] = lineData[0:]

    #Append the label to the labels array               
    labels.append(label)    
    if label=='largeDoses':
        labelsClass.append(3)
    elif label=='smallDoses':
        labelsClass.append(2)    
    else: 
        labelsClass.append(1)    

    index= index+1

#datingData = norm.normalizer(datingData)

# Plot the data
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.scatter(datingData[:,1], datingData[:,2],15.0*np.array(labelsClass),15.0*np.array(labelsClass))
fig.xlabel("Percentage of time playing videogames", fontsize=14)
fig.ylabel("Liters of ice cream consumed", fontsize=14)

fig2 = plt.figure(2)
ay = fig2.add_subplot(111)
ay.scatter(datingData[:,1], datingData[:,0],15.0*np.array(labelsClass),15.0*np.array(labelsClass))
plt.xlabel("Percentage of time playing videogames", fontsize=14)
plt.ylabel("Frequent flyer miles earned per year", fontsize=14)

plt.show()