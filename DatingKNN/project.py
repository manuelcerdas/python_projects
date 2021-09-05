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
minVals = []
ranges = []

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

datingData, minVals, ranges = norm.normalizer(datingData)

# Plot the data
fig, axes = plt.subplots (nrows=1, ncols=2)

axes[0].scatter(datingData[:,1], datingData[:,2],15.0*np.array(labelsClass),15.0*np.array(labelsClass))
axes[0].set_xlabel("Percentage of time playing videogames", fontsize=14)
axes[0].set_ylabel("Liters of ice cream consumed", fontsize=14)

axes[1].scatter(datingData[:,1], datingData[:,0],15.0*np.array(labelsClass),15.0*np.array(labelsClass))
axes[1].set_xlabel("Percentage of time playing videogames", fontsize=14)
axes[1].set_ylabel("Frequent flyer miles earned per year", fontsize=14)

fig.show()

dataLabels = ['not at all','in small doses','a lot']
#Get the data to evaluate from the user
frequentMiles=input("Frequent flyer miles owned per year: ")
playGames=input("Percentage of time spent playing video games: ") 
iceCream=input("Liters of ice cream eaten per year: ")
#frequentMiles=40920
#playGames=8.326976
#iceCream=0.953952

#normalize the user data
frequentMiles = (float(frequentMiles) - minVals[0]) / ranges[0]
playGames = (float(playGames) - minVals[1]) / ranges[1]
iceCream = (float(iceCream) - minVals[2]) / ranges[2]

#save user data as an array
userData = np.array([frequentMiles,playGames,iceCream])

result = cl.classify0(userData,datingData,labelsClass,3)

print (f"You will probably like this person {dataLabels[result-1]}")