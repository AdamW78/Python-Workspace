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

from SMSTexter import FindCellCarrier

server = smtplib.SMTP("smtp.gmail.com", 587)
carrier_dictionary = WebScraper.carrier_dictionary()


def send_message():
    """
    Main method for class, calls helper methods and actually sends text message

    Calls setup() and stores email from which to send text
    Fetches user's desired cell carrier to text on from carrier_setup()
    Creates recipient string email address by concatenating inputted phone number
    and the found email address for texting for selected cell carrier
    Ex: 1234567890@txt.att.net
    """
    auth = setup()
    user_carrier = carrier_setup()
    recipient = Constants.PHONE_NUMBER + str(list(carrier_dictionary[user_carrier])[0])
    try:
        server.sendmail(auth, recipient, Constants.MESSAGE)
    except smtplib.SMTPRecipientsRefused:
        print("Error: Could not send to that address")


def setup():
    """
    Initial setup method for sending texts

    Creates auth object with email provided from Constants file and app-password supplied from Constants file
    Opens a connection to gmail server
    Logs into gmail server
    :return: Email address as string from which text will be sent

    """
    auth = (Constants.EMAIL, Constants.PASSWORD)
    server.starttls()
    server.login(auth[0], auth[1])
    return auth[0]


def carrier_setup():
    """
    Calls search_carriers() to return either the found carrier or list of close matches to Constants.CARRIER
    Checks to see if search_carriers() returned a list or a single carrier
    If a single carrier, returns just that carrier
    If a list, calls get_carrier_selection(carrier_list) to obtain a single cell carrier - returns this carrier
    If 0, returns 0 - This means no similar carriers were found
    :return: 0 if no carrier was found, or user-selected cell carrier

    """
    carrier_list = search_carriers()
    if isinstance(carrier_list, str):
        return carrier_list
    else:
        carrier_selection = get_carrier_selection(carrier_list)
        if carrier_selection == 0:
            return 0
        return carrier_selection


def get_carrier_selection(close_matches):
    """
    Takes in a list of close matches for a cell carrier and gets the user to select the one they would like to text

    Prints "Could not find your exact input in our carrier list.", iterates through close_matches and prints each string
    Asks for yes/no input ("Is one of these correct? Enter \"y\" for yes or \"n\" for no: ") - is one of the printed values desired cell carrier
    If no, exit the program
    If yes, iterate through and print a numbered version of each string in list close_matches
    Asks for user input (numerical) to select the desired cell carrier
    Returns selected carrier
    :param close_matches: List of close matches returned from search_carriers() - list of strings
    :return: User carrier selection as string
    :raises TypeError Asks for a numerical input choice, this is raised if the input (string) cannot be converted to an int (usuallu means user did not input a number)
    :raises IndexError If the numerical input provided is out of bounds of list of options provided, this is raised
    :raises ValueError Asks for a yes/no user input, raised if user input is NOT: "Y"/"y" or "N"/"n"
    :
    """

    print("Could not find your exact input in our carrier list.")
    for i in range(len(close_matches)):
        if i == 0:
            print(f"Closest match was: \"{close_matches[0]}\"")
        else:
            print(f"Next closest match was: \"{close_matches[i]}\"")
    yes_no = input("Is one of these correct? Enter \"y\" for yes or \"n\" for no: ").casefold()
    if yes_no == "n":
        print("Unable to find your cell carrier. Exiting...")
        exit(0)
    elif yes_no == "y":
        for k in range(len(close_matches)):
            print(f"{k + 1}. {close_matches[k]}")
        number_choice = input("Please select the number of your cell carrier: ")
        try:
            num = int(number_choice)
        except ValueError:
            print(f"Error: Input \"{number_choice}\" is invalid. Exiting...")
            raise TypeError(f"User input \"{number_choice}\" failed to convert from string to integer.")
        if num > len(close_matches) or num <= 0:
            print(f"Error: Input \"{number_choice}\" is not a listed carrier. Exiting...")
            raise IndexError(f"User input \"{number_choice}\" was out of bounds for cell carrier list.")
        else:
            print(len(close_matches))
            carrier_choice = close_matches[num-1]
            print(f"Chosen carrier: {carrier_choice}")
            return carrier_choice
    else:
        print(f"Error: Input \"{yes_no}\" is invalid. Exiting...")
        raise ValueError("User input \"{yes_no}\" was invalid. Please enter \"y\" or \"n\".")


def search_carriers() -> str or list:
    """
    Method to search dictionary of cell carriers to find close matches or exact match for cell carrier from FindCellCarrier.find(number)

    Fetches cell carrier as a string using FindCellCarrier's find method
    Fetches list of cell carriers in carrier_dictionary
    Iterate through carriers in the carrier dictionary carrier-by-carrier
    If current cell carrier string is in carrier_dictionary, return the current carrier string
    Else, check if the current carrier string and the found carrier contain each other - if so, add it to close matches
    Then, return a list of the 5 most lexicographically similar strings to user_carrier from carrier_dictionary
    :return: List close_matches of 5 most lexicographically similar strings to user_carrier OR exact match
    """
    user_carrier = FindCellCarrier.get_carrier(Constants.PHONE_NUMBER)
    keys = list(carrier_dictionary.keys())
    for key in keys:
        if user_carrier == key:
            return user_carrier
        elif (key.find(user_carrier) != -1) or (user_carrier.find(key) != -1):
            return key
    return difflib.get_close_matches(user_carrier, list(carrier_dictionary.keys()), n=5, cutoff=0.2)


def main():
    send_message()


main()
