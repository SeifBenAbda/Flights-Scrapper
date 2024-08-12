"""
    Responsible to Transform Flights from Json Format to List of Flight with Details
"""
from classes.flight_class import Flight
from classes.flight_details import FlightDetails


class FlightManager:
    def __init__(self, flight_data):
        self.flight_data = flight_data

    """
          This is Responsible to Create a List of 'Flight' and Each Flight has 4 Attributes Including the Flight Details 
          See Classes 'Flight' and 'FlightDetails' for More Details and Examples
      """

    def setup_flights(self):
        flight_data_json = self.flight_data
        flights = []
        for flight_data in flight_data_json:
            flight = Flight(
                price=flight_data['Price'],
                operator=flight_data['Operator'],
                outward_flight_details=self.setup_flight_details(flight_data["Flight Details 1"]),
                return_flight_details=self.setup_flight_details(
                    flight_data["Flight Details 2"]) if "Flight Details 2" in flight_data else None
            )
            flights.append(flight)
        return flights


    def setup_flight_details(self,flight_details_data):
        return FlightDetails(
            airport_start= self.get_airport_data(flight_details_data["Outbound_Flight_AirPorts"],True),
            airport_destination=self.get_airport_data(flight_details_data["Outbound_Flight_AirPorts"],False),
            take_off_time=flight_details_data["Take Off Time"],
            landing_time=flight_details_data["Landing Time"],
            duration=flight_details_data["Duration"],
            extra_days=flight_details_data["Extra Days Trip"],
            operator_images=flight_details_data["Image 1"],
            number_stops=flight_details_data["Number Stops"],
            stops=[]
        )


    @staticmethod
    def get_airport_data(airports_value,is_start_airport):
        # Split the string into parts
        parts = airports_value.split('\n')

        # Extract the airport code and name dynamically
        airport_code = parts[0 if is_start_airport else 2][:3]  # Extract the first 3 characters for the code
        airport_name = parts[0 if is_start_airport else 2][3:].strip()  # Extract the remainder for the name and strip any surrounding whitespace

        # Combine code and name into a formatted string
        airport_details = f"{airport_code} ({airport_name})"

        return airport_details