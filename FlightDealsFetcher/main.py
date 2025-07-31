#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch

def main():
    flight_data_instance = FlightData()
    sheet_data = flight_data_instance.sheet_data
    pprint(sheet_data)
    flightSearch=FlightSearch()#instance
    for i in sheet_data:
        if i['iataCode']=='':
             i['iataCode']=flightSearch.get_iata_code(i['city'])
    pprint(sheet_data)        
if __name__ == "__main__":
    main()
