# Normalize the data
# FORMULA Normalized value = (value-min) / (max-min)

import numpy as np

def normalizer (dataSet):  
    # find tne mins and maxs
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    
    #get the ammount of rows in the dataset to create the tiles
    numRows = dataSet.shape[0]

    # Create an array to store the results
    # REMEMBER: parameters in Python are passed by reference
    normalizedData = np.zeros(dataSet.shape)

    normalizedData = dataSet - np.tile(minVals,(numRows,1))
    normalizedData = normalizedData / np.tile(ranges,(numRows,1))

    return normalizedData, minVals, ranges;

