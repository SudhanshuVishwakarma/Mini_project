import phonenumbers
from phonenumbers import timezone, geocoder, carrier 

number = input("Enter your Number (+91):")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone, "en")
registration = geocoder.description_for_number(phone, "en")

print(time)
print(phone)
print(carr)
print(registration)
