import csv
import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
from sets import Set

pickup_df = pd.read_csv('yellow_tripdata_2015-12.csv')

pickup_df = pickup_df[(pickup_df.pickup_latitude != 0) & (pickup_df.pickup_longitude != 0)]

test = pickup_df.ix[:,['pickup_longitude', 'pickup_latitude']]

# with open('yellow_tripdata_2015-12.csv', 'rb') as csvfile:
#      reader = csv.reader(csvfile)
#      i = 0
#      for row in reader:
#          i = i + 10
#          if i == 10:
#              continue
#          if i > 1000:
#             break
#
#          if row[5] != '0':
#              X.append([float(row[5]), float(row[6])])
#
#
# test = np.asarray(X)

#y_pred = cluster.KMeans(n_clusters=30, random_state=random_state).fit_predict(test)

"""
0.009 degree == 1 km

0.0045 degree == 500m
"""

dbscan_clusters = cluster.DBSCAN(eps=0.0009, min_samples=100)
dbscan_clusters.fit(test)

print dbscan_clusters.labels_.size

test['cluster'] = dbscan_clusters.labels_

label_set = Set(dbscan_clusters.labels_)
print label_set

columns = ['pickup_longitude','pickup_latitude', 'size', 'label']
regions = pd.DataFrame(columns=columns)

for label in label_set:
    if label != -1:
        cluster_df = test[test.cluster == label]
        mean_lat = np.mean(cluster_df.pickup_latitude)
        mean_lng = np.mean(cluster_df.pickup_longitude)
        # print mean_lat
        # print mean_lng
        # print cluster_df.size

        regions = regions.append(pd.DataFrame([[mean_lng, mean_lat, cluster_df.size, label]], columns=columns), ignore_index=True)

print regions

regions.to_csv('regions.csv')

plt.scatter(regions['pickup_longitude'], regions['pickup_latitude'], c=regions['label'])
plt.title("Clustering 30 on 1000 points")
plt.show()
