# Taxi Regions of Interest Clustering

## Data
NYC Green Cab December 2015

## Algorithms Choosing
There are many clustering algorithms to choose from. KMeans is one of the most used clustering algorithm.
But in this case, KMeans is not the best choice, since the location data is not evenly separate which will make the clusters size various dramatically and there will also have a large amount of clusters. This will greatly weaken the performance of KMeans Algorithm.

Therefore I have chosen DBSCAN algorithm. DBSCAN is a density based algorithm, which uses density as number of points within a specified radius where point is a core point. In this case is a perfect fit for our problem.

There a two important parameters for DBSCAN algorithm.
1. The maximum distance between two samples for them to be considered as in the same neighborhood.
  I have chosen 50 meters (about 0.00045 degree in longitude or latitude) in my solution.
2. The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.
In this case I chosen the number of 50.


## My Solution

1. Cleaning the data, remove useless data which don't have pickup location information and take out only longitude and latitude data to build a new data set for the following learning process.

2. Dividing the map into different areas. Since training the whole dataset will required huge amount of memory and computation resources.

3. Training each small area and calculate the center coordinate of each cluster generated. Then combine all the data to final result.

4. Visualizing the regions of interests of green cab on map using d3.js and Mapbox.


## Visualizing
![Visualizing](shttps://github.com/NGCyang/TaxiRegionsofInterestClustering/blob/master/visualizing.png)
