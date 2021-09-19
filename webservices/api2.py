# API via Python
import urllib.request, urllib.parse, urllib.error
import json

# Using Google Maps API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Address: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    urlhandle = urllib.request.urlopen(url)
    data = urlhandle.read().decode() # data is now a string since its been decoded
    print('Retrieved', len(data), 'characters')

    try:
        res = json.loads(data)
    except:
        res = None
    
    if not res or 'status' not in res or res['status'] != 'OK':
        print('**** Failure To Retrieve ****')
        print(data)
        break

    lat = res["results"][0]["geometry"]["location"]["lat"]
    lng = res["results"][0]["geometry"]["location"]["lng"]

    print('lat:', lat, 'lng:', lng)

    location = res["results"][0]['formatted_address']
    print(location)