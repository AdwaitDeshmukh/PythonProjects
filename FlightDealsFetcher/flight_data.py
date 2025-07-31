import requests
from pprint import pprint

import requests

class FlightData:
    API_GET = "https://api.sheety.co/e7e36a5ace33f7e20350048cd9b28918/flightDeals/prices"

    def __init__(self):
        self.sheet_data = self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(self.API_GET)
        response.raise_for_status()
        data = response.json()["prices"]
        return data  


