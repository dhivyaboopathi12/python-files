import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier

number_str = "+91994253316"
number = ph.parse(number_str)
print(timezone.time_zones_for_number(number))
print("list of details..")
print(carrier.name_for_number(number,"en"))
print(geocoder.description_for_number(number,"en"))

 

