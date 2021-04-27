import operator
import matplotlib.pyplot as plt
import json
import numpy as np
import classifier as cl

#Read the training data json
filename = 'data/movies.json'

with open (filename) as f:
    data = json.load (f)

kicks = []
kisses = []
datum = []
trainingData = []
labels = []
colors = []

#Read the training data for plotting and using the classifier
for movie in data["movies"]:
    #Adding data for the plot
    kisses.append (movie["kisses"])
    kicks.append (movie["kicks"]) 
    plt.annotate(movie["title"],(movie["kicks"],movie["kisses"]))    
    colors.append(5)

    #Formatting the json data for use in the classifier
    datum = [] 
    datum.append (movie["kisses"])
    datum.append (movie["kicks"])
    trainingData.append (datum)      
    labels.append (movie["type"])

#Read the movies to classify json
filename = 'data/newMovies.json'

with open (filename) as f:
    newMovies = json.load (f)

#Read the movies to classify for plotting 
for movie in newMovies["movies"]:
    #Adding data for the plot
    kisses.append (movie["kisses"])
    kicks.append (movie["kicks"]) 
    plt.annotate(movie["title"],(movie["kicks"],movie["kisses"]))    
    colors.append (25)

for movie in newMovies["movies"]:    
    datum = [] 
    datum.append (movie["kisses"])
    datum.append (movie["kicks"])    
    print (f"{movie['title']} is a {cl.classify0 (np.array(datum),np.array(trainingData),labels,3)} movie")
    

#Show the plot with the test data
plt.scatter(kicks,kisses,s=100,c=colors)
plt.title("Movies", fontsize=24)
plt.xlabel("Kicks", fontsize=14)
plt.ylabel("Kisses", fontsize=14)
plt.show()