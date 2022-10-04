import requests
from bs4 import BeautifulSoup, NavigableString

site = "https://avtech.com/articles/138/list-of-email-to-sms-addresses/"

response = requests.get(site)
soup = BeautifulSoup(response.content, "html.parser")
body = soup.body
table = body.find(class_="container-fluid-max")
text_to_mail_addresses = dict({"": []})
for email in table.find_all("p", style="padding-left: 30px;"):
    full_mail_address = str(email.string).split("@")
    cur_carrier = ""
    for p in email.previous_siblings:
        search_for_carrier = str(p).find("<strong>")
        if search_for_carrier != -1:
            search = str(p).split("<strong>")
            search = search[1].split("</strong>")
            cur_carrier = search[0]
            break
    mail_address = ""
    try:
        mail_address = "@"+full_mail_address[1]
    except IndexError:
        continue
    email_list = []
    if cur_carrier in text_to_mail_addresses:
        email_list = text_to_mail_addresses[cur_carrier]
    email_list.append(mail_address)
    text_to_mail_addresses[cur_carrier] = email_list
