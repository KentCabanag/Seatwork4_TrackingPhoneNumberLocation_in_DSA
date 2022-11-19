import phonenumbers

from yourPhoneNumber import number

from phonenumbers import geocoder

TheNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(TheNumber, "en")
print(yourLocation)


# get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))



#CTTO https://www.youtube.com/watch?v=Geisa_ib5hs&t=506s