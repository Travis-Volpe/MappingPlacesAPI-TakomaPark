# API Key: AIzaSyBFDjlbx8jNOc1Cdqni4tri0Xka_fqjGc8

import googlemaps
import json

api_url = r'https://maps.googleapis.com/maps/api/geocode/xml?address={}'.format(address)
r = requests.get(api_url)
b = BeautifulSoup(r.text, 'xml')

b.find('status').text

address_components = b.find_all('address_component')
for address in address_components:
    address_type = address.find('type').text
    if 'postal_code' in address_type:
        print(address.find('long_name').text)

latitude = b.find('location').find('lat').text
longitude = b.find('location').find('lng').text

gmaps = googlemaps.Client(key='INSERTAPIKEYHERE')
gmaps.reverse_geocode((latitude,longitude))
gmaps.places('Takoma Park', location=(latitude, longitude), radius=1000)

address = '6917 Laurel Ave, Takoma Park, MD 20912'
api_json_url = r'https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(address)
r = requests.get(api_json_url)

j = json.loads(r.text)
j['results'][0]['geometry']['location']['lat']
j['results'][0]['geometry']['location']['lng']
