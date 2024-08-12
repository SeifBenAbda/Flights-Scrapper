from dataclasses import asdict
from classes.flights_manager import FlightManager
from classes.kayak_class import KayakService
import json



class ScrapService:
    def __init__(self, selected_platform,data):
        self.selected_platform = selected_platform
        self.data = data

    def get_flights(self):
        if self.selected_platform=='kayak':

            #Get Data From Javascript
            origin = self.data.get('from_airport')
            destination = self.data.get('landing_airport')

            #Hard Code Dates
            kayak_instance = KayakService(origin,destination,"2024-06-27","2024-06-28")

            # Scrapped Data
            flights_data = kayak_instance.scrap_data()

            #Flight Manager Instance
            fm = FlightManager(flights_data)

            #Create List of Flights
            flights_list = fm.setup_flights()

            #Convert the List of Flight to List of Dict.
            flights_dict_list = [asdict(flight) for flight in flights_list]

            # Convert List of Dict to JSON
            flights_json = json.dumps(flights_dict_list, indent=4)


            print(flights_json)
            return flights_json

        return {"Flights":None}







