#
# Originally Sourced from:
# Author D3ISM3
# Edited by Adam W
# https://gist.github.com/D3ISM3/743d2119562c3e01d9e09baf8c5df328#file-sendtextmessage-py
# Modified to support multiple senders
# Modified to simplify for specific use-case (Sending rush text-messages)
#

import smtplib
# import sys

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com",
    "acs-wireless": "@paging.acswireless.com",
    "advantage-communications": "@advantagepaging.com"


}

EMAIL = "Code.AdamW78@gmail.com"
PASSWORD = "ytlrdemjuebgloyi"
PHONE_NUMBER = "5712629202"
CARRIER = "att"
MESSAGE = "This is a test text message."

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    try:
        server.sendmail(auth[0], recipient, message)
    except smtplib.SMTPRecipientsRefused:
        print("Error: Could not send to that address")


def main():
    # if len(sys.argv) < 4:
    #    print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
    #    sys.exit(0)
    send_message(PHONE_NUMBER, "att", MESSAGE)
    send_message(PHONE_NUMBER, "verizon", MESSAGE)
    send_message(PHONE_NUMBER, "tmobile", MESSAGE)


main()
