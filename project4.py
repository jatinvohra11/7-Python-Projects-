import phonenumbers
from phonenumbers import geocoder, carrier, timezone
number = input("Enter phone number with country code")
try:
    parsed_number = phonenumbers.parse(number)

    valid = phonenumbers.is_valid_number(parsed_number)

    location = geocoder.description_for_number(parsed_number, 'en')

    service_provider = carrier.name_for_number(parsed_number, 'en')

    timezone = timezone.time_zones_for_number(parsed_number)

    print("\n Phone Number Details: ")
    print(f" Valid: {valid}")
    print(f" Location: {location}")
    print(f" Carrier: {service_provider}")
    print(f" Timezone: {timezone}")

except Exception as e:
    print("Error: ", e)