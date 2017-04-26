import csv
import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt



"""
['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'RatecodeID', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']
"""

taxi_data_df = pd.read_csv('yellow_tripdata_2015-12.csv')
pickup_data_df = taxi_data_df[['pickup_longitude', 'pickup_latitude']]

pickup_data_df = pickup_data_df[(pickup_data_df.pickup_latitude != 0) & (pickup_data_df.pickup_longitude != 0)]


pickup_data_df.to_csv('cleaned_data.csv', sep='\t')

'''
with open('cleaned_data.csv', 'w') as csvfile:
    fieldnames = ['pickup_longitude', 'pickup_latitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(pickup_data)
'''
