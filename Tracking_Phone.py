import phonenumbers

from yourPhoneNumber import number

from phonenumbers import geocoder

TheNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(TheNumber, "en")
print(yourLocation)