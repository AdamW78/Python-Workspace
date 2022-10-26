from twilio.rest import Client
from SMSTexter import Constants


def get_carrier(number):
    url = f"https://lookups.twilio.com/v2/PhoneNumbers/{number}"
    account_sid = Constants.TWILIO_SID
    auth_token = Constants.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    phone_number = client.lookups \
        .v1 \
        .phone_numbers(number) \
        .fetch(type=['carrier'])
    print(phone_number.carrier['name'])
    return phone_number.carrier['name']
