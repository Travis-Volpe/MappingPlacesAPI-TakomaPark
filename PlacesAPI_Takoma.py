#Takoma Beverage Company
#ChIJF0626YLIt4kR0Q3xzWExGnk
#https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJF0626YLIt4kR0Q3xzWExGnk&fields=photos,formatted_address,name,rating,price_level,opening_hours,reviews,geometry&key=AIzaSyCSp7eUtne91wcK2thVDc7WPbUnIjOu2iM
#https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Takoma%20Beverage%20Company&inputtype=textquery&fields=photos,formatted_address,name,rating,price_level,reviews,opening_hours,geometry&key=AIzaSyCSp7eUtne91wcK2thVDc7WPbUnIjOu2iM

import requests
import json
import time

#https://python.gotrained.com/google-places-api-extracting-location-data-reviews/
#Create a dummy class object to access API key

class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = 'AIzaSyCSp7eUtne91wcK2thVDc7WPbUnIjOu2iM'

#Add search funcitonailiy to class - enter a GPS coordinate and radius and will return all nearby places
# Change so that it searches for just
    def search_places_by_coordinate(self, name, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'name': name,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details


api = GooglePlaces('AIzaSyCSp7eUtne91wcK2thVDc7WPbUnIjOu2iM')

places = api.search_places_by_coordinate("Takoma Park", "1000", "restaurant")

fields = ['name','formatted_address', 'price_level']

for place in places:
    details = api.get_place_details(place['place_id'], fields)
    try:
        name = details['result']['name']
    except KeyError:
        name = ""
    try:
        address = details['result']['formatted_address']
    except KeyError:
        address = ""
    try:
        price_level = details['result']['price_level']
    except KeyError:
        price_level = ""

    print("########## PLACE DETAILS ##########")
    print("Name:", name)
    print("Address:", address)
    print("Price Level:", price_level)

# Export to df / csv

# Vizualize

# Combine with parcel Dataset

# Use Geopandas and Shapely to map

# Apply mgwr
