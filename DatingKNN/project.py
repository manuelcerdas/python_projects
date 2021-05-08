import matplotlib.pyplot as plt
import numpy as np
import classifier as cl
import normalizer as norm

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

    index= index+1

#datingData = norm.normalizer(datingData)

# Plot the data
print (datingData[:1])

