from dataclasses import dataclass, field, asdict
from typing import List, Optional
"""
    Class 'Stops' :
        Attribute 1 : stops_at : Indicates where a Flight Stops
        Attribute 2 : stop_duration : Indicates how long a Flight Stops
"""

class Stops:
    def __init__(self, stop_at, stop_duration):
        self.stop_at = stop_at
        self.stop_duration = stop_duration

    def __repr__(self):
        return f"Stops(stop_at='{self.stop_at}', stop_duration='{self.stop_duration}')"



"""
    This Class 'FlightDetails' is Responsible to Show the Flight Details (One-Way) 
    Example : A RoundTrip 'Flight' From Frankfurt to Madrid has 2 'FlightDetails' Instances since it's a RoundTrip
"""


@dataclass
class FlightDetails:
    airport_start: str
    airport_destination: str
    take_off_time: str
    landing_time: str
    extra_days: int
    duration: str
    operator_images: List[str]
    number_stops: int
    stops: List[str] = field(default_factory=list)


    #Add Stop to a Flight Details
    def add_stop(self, stop):
        self.stops.append(stop)

    def __repr__(self):
        return (f"Flight(airport_start='{self.airport_start}', airport_destination='{self.airport_destination}', "
                f"date_start='{self.date_start}', date_landing='{self.date_landing}', over_days={self.over_days}, "
                f"stops={self.stops})")