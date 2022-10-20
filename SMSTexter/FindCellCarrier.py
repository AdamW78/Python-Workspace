import json
import asyncio

import httpx
import requests



def test_open_page(scrape_url):

    url = "https://scrapeninja.p.rapidapi.com/scrape"

    payload = {"url": scrape_url}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9d4b66e447mshbcc599e9517c35cp1d4ae9jsnf053e10ee522",
        "X-RapidAPI-Host": "scrapeninja.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response


def get_carrier(number):
    url = 'https://api.telnyx.com/v1/phone_number/1' + str(number)
    # s = requests.Session()
    # scraper = cloudscraper.create_scraper()
    # json_text = scraper.get(url).text
    # client = httpx.Client(http2=True)
    # response = await client.get(url)
    response = test_open_page(url)
    print(response.text.find("carrier"))
    # json_text = json.loads(response_text)
    # carrier = json_text["carrier"]["name"]
    # return carrier

asyncio.run(get_carrier("5712629202"))
