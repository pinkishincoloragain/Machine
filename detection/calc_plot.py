import pandas as pd
from geopy.geocoders import Nominatim
import osmnx as ox

geolocoder = Nominatim(user_agent = 'South Korea')

def geocoding(address):
    geo = geolocoder.geocode(address)
    crd = (geo.latitude, geo.longitude)
    print(crd)
    return crd