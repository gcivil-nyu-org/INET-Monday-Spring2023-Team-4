import os
import requests

def get_locations():
    #send GET request to specified url (endpoint)
    #returns requests.Response object
    endpoint = 'https://data.cityofnewyork.us/resource/if26-z6xq.json'
    r = requests.get(endpoint, None)
    #converts the JSON response (requests.Response object) from the API endpoint to a Python dictionary

    locations = r.json()
    return locations
