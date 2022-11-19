import phonenumbers

from yourPhoneNumber import number

from phonenumbers import geocoder

key = '866d0e93ffad45968a0f687fe6620ec9'

TheNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(TheNumber, "en")
print(yourLocation)


# get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

#CTTO https://www.youtube.com/watch?v=Geisa_ib5hs&t=506s