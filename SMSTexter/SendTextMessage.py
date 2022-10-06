#
# Originally Sourced from:
# Author D3ISM3
# Edited by Adam W
# https://gist.github.com/D3ISM3/743d2119562c3e01d9e09baf8c5df328#file-sendtextmessage-py
# Modified to support multiple senders
# Modified to simplify for specific use-case (Sending rush text-messages)
#

import smtplib
import Constants
import WebScraper
import difflib

carrier_dictionary = WebScraper.carrier_dictionary()
server = smtplib.SMTP("smtp.gmail.com", 587)


def send_message():
    auth = setup()
    user_carrier = carrier_setup()
    recipient = Constants.PHONE_NUMBER + str(list(carrier_dictionary[user_carrier])[0])
    try:
        server.sendmail(auth, recipient, Constants.MESSAGE)
    except smtplib.SMTPRecipientsRefused:
        print("Error: Could not send to that address")


def setup():
    auth = (Constants.EMAIL, Constants.PASSWORD)
    server.starttls()
    server.login(auth[0], auth[1])
    return auth[0]


def carrier_setup():
    carrier_list = search_carriers()
    if isinstance(carrier_list, str):
        return carrier_list
    else:
        return get_carrier_selection(carrier_list)


def get_carrier_selection(close_matches):
    print("Could not find your exact input in our carrier list.")
    for i in range(len(close_matches) - 1):
        if i == 0:
            print(f"Closest match was: \"{close_matches[0]}\"")
        else:
            print(f"Next closest match was: \"{close_matches[i]}\"")
    yes_no = input("Is one of these correct? Enter \"y\" for yes or \"n\" for no: ").casefold()
    if yes_no == "n":
        print("Unable to find your cell carrier. Exiting...")
        return 0
    elif yes_no == "y":
        for k in range(len(close_matches)-1):
            print(f"{k + 1}. {close_matches[k]}")
        number_choice = input("Please select the number of your cell carrier: ")
        num = -1
        int (number_choice)
        try:
            num = int(number_choice)
        except:
            print(f"Error: Input \"{one_two_three}\" is invalid. Exiting...")
            return 0
        if num > len(close_matches):
            print(f"Error: Input \"{one_two_three}\" is not a listed carrier. Exiting...")
            return 0
        else:
            carrier_choice = close_matches[num-1]
            print(f"Chosen carrier: {carrier_choice}")
            return carrier_choice
    else:
        print(f"Error: Input \"{yes_no}\" is invalid. Exiting...")
        return 0


def search_carriers():
    user_carrier = Constants.CARRIER
    keys = list(carrier_dictionary.keys())
    if user_carrier in keys:
        return user_carrier
    else:
        close_matches = difflib.get_close_matches(user_carrier, list(carrier_dictionary.keys()), n=5, cutoff=0.2)
        return close_matches


def main():
    send_message()


main()
