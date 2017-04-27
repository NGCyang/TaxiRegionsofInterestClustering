import pandas as pd

"""
['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'RatecodeID', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']
"""

taxi_data_df = pd.read_csv('green_tripdata_2015-12.csv')

taxi_data_df = taxi_data_df.ix[:,['Pickup_longitude', 'Pickup_latitude']]
#taxi_data_df = taxi_data_df.ix[:,['pickup_longitude', 'pickup_latitude']]

taxi_data_df = taxi_data_df[(taxi_data_df.Pickup_latitude != 0) & (taxi_data_df.Pickup_longitude != 0)]
#taxi_data_df = taxi_data_df[(taxi_data_df.pickup_latitude != 0) & (taxi_data_df.pickup_longitude != 0)]

#print taxi_data_df

#
# pickup_data_df = taxi_data_df[['pickup_longitude', 'pickup_latitude']]
#
# pickup_data_df = pickup_data_df[(pickup_data_df.pickup_latitude != 0) & (pickup_data_df.pickup_longitude != 0)]
#

taxi_data_df.to_csv('green_cleaned_data.csv')

'''
with open('cleaned_data.csv', 'w') as csvfile:
    fieldnames = ['pickup_longitude', 'pickup_latitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(pickup_data)
'''
