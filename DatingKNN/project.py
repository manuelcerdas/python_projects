import matplotlib.pyplot as plt
import numpy as np
import classifier as cl

#Read the training data json
filename = 'data/datingTestSet.txt'

#Read the file as an array of text lines
with open (filename) as f:
    data = f.readlines()

#read the first line of the data and make it an array
firstLine = data[0].strip()

#see how many numeric columns the array has (only the last column is string).  The colums are separated by tabs
gapCount = firstLine.count("\t")

datingData = np.array([])
labels =  []

for line in data:
    line = line.strip()
    splitLine = line.split("\t");

    #split the line into numeric data and label
    lineData = splitLine[0:gapCount]
    #the last column is the label
    label = splitLine[-1]
    
    aux=[]
    aux.append(lineData)
    datingData = np.append(datingData,lineData,axis=1)    
               
    labels.append(label)

print (datingData)