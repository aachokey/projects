from geopy.geocoders import Nominatim
import pandas as pd

import geopandas as gp
from shapely.geometry import Point


cccl_permits = pd.read_csv("cleaned_permits.csv", low_memory=False)

geolocator = Nominatim()

# cccl_permits['Y'] = cccl_permits.Y.apply(pd.to_numeric)
# cccl_permits['X'] = cccl_permits.X.apply(pd.to_numeric)

cccl_permits['coordinates'] = cccl_permits.apply(
	lambda z: (z.X, z.Y), axis=1
	)



def reverse_geocode(coords):
	location = geolocator.geocode(coords)
	return location.county

cccl_permits['county'] = cccl_permits.coordinates.apply(reverse_geocode)

print(cccl_permits)