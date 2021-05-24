import numpy as np

def classify0 (newPoint, dataSet, labels, k):   
    # Get the ammount of rows in the data set         
    numRows = dataSet.shape[0]

    #Create a matrix the same size as the data set, but in this case all the rows are the new point
    newSet = np.tile (newPoint,(numRows,1))    

    # we use Euclid to obtain the distance
    # if the point are (a,d) and (b,c) then the distance is ((a-b)**2 + (d-c)**2) **0.5
        
    #Calulating the (a-b)**2
    firstStep = (newSet - dataSet) ** 2
    
    #Now add the results in the previous step (adding the squares)
    secondStep = firstStep.sum(axis=1)

    # get the square root
    distances = secondStep ** 0.5

    # get the sorted indexes of the distances
    sortedDistancesIndexes = distances.argsort()

    #Create a dictionary to store the results
    labelCount = {}
      
    for i in range(k):        
        voteLabel = labels[sortedDistancesIndexes[i]]        
        labelCount[voteLabel] = labelCount.get(voteLabel,0)+1

   
    sortedLabelCount = sorted(labelCount,key=labelCount.get)

    return (sortedLabelCount[0])
        

    
        
            
    
   