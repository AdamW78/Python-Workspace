import requests
from bs4 import BeautifulSoup
import Constants
from SMSTexter import DictChecker, DictReader


def open_connection(site):
    """
    Creates a connection to website from which carriers and text-to-email addresses are pulled

    :param site: URL for website from which cell carrier dictionary will be created
    :return: Body of website from BeautifulSoup
    """
    response = requests.get(site)
    if Constants.DEBUG:
        print(f"Response from \"f{site}\" {response}")
    soup = BeautifulSoup(response.content, "html.parser")
    if Constants.DEBUG:
        print(f"BeautifulSoup Object Content: {soup}")
    body = soup.body
    if Constants.DEBUG:
        print(f"BeautifulSoup Body object: {body}")
    return body


def create_carrier_dictionary(body):
    """
    Creates dictionary object from body BeautifulSoup object of cell carriers and their text-to-email addresses

    Fetches table object by finding the first HTML object in the <body> with class "container-fluid-max"
    Creates dictionary of strings and lists
    Iterates through the table by each <p> HTML object with style "padding-left: 30px;" (Email address)
    Convert each email from a NavigableString BeautifulSoup object to a string object
    Navigates the previous HTML objects from each email address until a <strong> HTML element is found (Cell carrier)
    Creates string from each previous HTML <p> object until it finds a string with <strong> in it
    Takes contents of <strong> tag, formats, and updates cur_carrier
    Use cur_carrier as key for text_to_mail_addresses dict to update values
    Returns dictionary containing String keys and Lists of string values
    :param body: BeautifulSoup object representing the contents of HTML body tag
    :return: Dictionary object containing cell carriers (strings) and lists of text-to-mail addresses (list of strings)
    """
    table = body.find(class_="container-fluid-max")
    text_to_mail_addresses = dict()
    for email in table.find_all("p", style="padding-left: 30px;"):
        full_mail_address = str(email.string).split("@")
        cur_carrier = ""
        for p in email.previous_siblings:
            search_for_carrier = str(p).find("<strong>")
            if search_for_carrier != -1:
                search = str(p).split("<strong>")
                search = search[1].split("</strong>")
                cur_carrier = search[0]
                ampersand_search = cur_carrier.find("&amp;")
                if ampersand_search != -1:
                    cur_carrier = cur_carrier.replace("&amp;", "&")
                if Constants.DEBUG:
                    print(f"Found carrier {cur_carrier}, ", end="")
                break
        try:
            mail_address = "@" + full_mail_address[1]
            if Constants.DEBUG:
                print(f"updating with text-to-email address \"{mail_address}\".")
        except IndexError:
            continue
        email_list = []
        if cur_carrier in text_to_mail_addresses:
            email_list = text_to_mail_addresses[cur_carrier]
        email_list.append(mail_address)
        text_to_mail_addresses[cur_carrier] = email_list
    return text_to_mail_addresses


def fetch_carrier_dictionary_local() -> dict:
    carrier_dict_file = DictChecker.get_csv_dict()
    return DictReader.read(carrier_dict_file)


def carrier_dictionary():
    if Constants.DEBUG or (not DictChecker.has_csv_dict()):
        _carrier_dictionary = create_carrier_dictionary(open_connection(Constants.WEBSITE))
        if Constants.DEBUG:
            return fetch_carrier_dictionary_local()

    else:
        return fetch_carrier_dictionary_local()
    return _carrier_dictionary
