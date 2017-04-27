import csv
import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
from sets import Set
import time
import os

"""
yellow_tripdata_2015-12
#total  33880368
#, nrows=1000000

green_tripdata_2015-12
total  4824870
"""
def clustering(pickup_df):

    #pickup_df = pickup_df[(pickup_df.pickup_latitude != 0) & (pickup_df.pickup_longitude != 0)]

    test = pickup_df.ix[:,['pickup_longitude', 'pickup_latitude']]
    #test = pickup_df.ix[:,['pickup_longitude', 'pickup_latitude']]
    """
    0.009 degree == 1 km

    0.0045 degree == 500m
    """

    dbscan_clusters = cluster.DBSCAN(eps=0.00045, min_samples=100)
    dbscan_clusters.fit(test)

    print dbscan_clusters.labels_.size

    test['cluster'] = dbscan_clusters.labels_

    label_set = Set(dbscan_clusters.labels_)
    print label_set

    columns = ['pickup_longitude','pickup_latitude', 'size', 'label']
    regions = pd.DataFrame(columns=columns)

    # for label in label_set:
    #     if label != -1:
    #         #time.sleep(1000)
    #         cluster_df = test[test.cluster == label]
    #         mean_lat = np.mean(cluster_df.pickup_latitude)
    #         mean_lng = np.mean(cluster_df.pickup_longitude)
    #         # print mean_lat
    #         # print mean_lng
    #         # print cluster_df.size
    #         regions = regions.append(pd.DataFrame([[mean_lng, mean_lat, cluster_df.size, label]], columns=columns), ignore_index=True)
    #
    # regions.to_csv('green_regions.csv')
    return regions

def parting_clustering(pickup_df):
    test = pickup_df.ix[:,['pickup_longitude', 'pickup_latitude']]

    columns = ['pickup_longitude','pickup_latitude', 'size', 'label']
    regions = pd.DataFrame(columns=columns)

    """
    Dividing Areas

    40.60  - 40.9
    73.7 - 74.1
    [lower_latitude, upper_latitude, lower_longitude, upper_longtitude]

    [[-90.0, +90.0, 74.1, +180.0],
     [-90.0, +90.0, -180.0, 73.7],
     [-90.0, 40.6, 73.7. 74.1],
     [40.9, +90.0, 73.7, 74.1],
     [40.6, 40.62, 73.7, ],

    ]

    """
    areas = get_areas()

    for area in areas:
        # time.sleep(1)
        print(area)
        area_data = test[(test.pickup_latitude >= area[0]) & (test.pickup_latitude < area[1]) & (test.pickup_longitude >= area[2]) & (test.pickup_longitude < area[3])]
        print(area_data.size)
        if area_data.size == 0:
            continue
        dbscan_clusters = cluster.DBSCAN(eps=0.00045, min_samples=200)
        dbscan_clusters.fit(area_data)
        area_data['cluster'] = dbscan_clusters.labels_

        label_set = Set(dbscan_clusters.labels_)

        for label in label_set:
            if label != -1 and label != -1.0:
                # time.sleep(1)
                cluster_df = area_data[area_data.cluster == label]
                mean_lat = np.mean(cluster_df.pickup_latitude)
                mean_lng = np.mean(cluster_df.pickup_longitude)

                regions = regions.append(pd.DataFrame([[mean_lng, mean_lat, cluster_df.size, label]], columns=columns), ignore_index=True)
    #regions.to_csv('regions.csv')
    if not os.path.isfile('yellow_regions.csv'):
       regions.to_csv('yellow_regions.csv')
    else: # else it exists so append without writing the header
        regions.to_csv('yellow_regions.csv',mode = 'a',header=False)

    return regions

def get_areas():
    areas = [[-90.0, +90.0, -180, -74.1],[-90.0, +90.0, -73.7, 180],[-90.0, 40.6, -74.1, -73.7],[40.9, +90.0, -74.1, -73.7]]

    for lat in range(0,100):
        if 40.6 + 0.01 * lat <= 40.9:
            lower_lat = 40.6 + (lat - 1) * 0.01
            higher_lat = 40.6 + lat * 0.01
            for lon in range(0,200):
                if -74.1 + 0.01 * lon <= -73.7:
                    lower_lon = -74.1 + 0.01 * (lon - 1)
                    higher_lon = -74.1 + 0.01 * lon
                    areas.append([lower_lat, higher_lat, lower_lon, higher_lon])

    return areas

def plot(regions):
    #plt.scatter(test['pickup_longitude'], test['pickup_latitude'])
    plt.scatter(regions['pickup_longitude'], regions['pickup_latitude'], c=regions['label'])
    plt.title("Clustering 30 on 1000 points")
    plt.show()

if __name__ == "__main__":
    pickup_df = pd.read_csv('cleaned_data.csv')
    result = parting_clustering(pickup_df)
    plot(result)

    # plt.scatter(pickup_df['pickup_longitude'], pickup_df['pickup_latitude'])
    # plt.show()
