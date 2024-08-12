from dataclasses import dataclass, field, asdict
from typing import Optional

from classes.flight_details import FlightDetails

"""
    Class 'Flight' has 4 Attributes :
        - Attribute 1 : Price of the Flight
        - Attribute 2 : Operator of the Flight (Company) | In Case of Multiple Companies Involved (Multi-Companies : Output (Kayak.de))
        - Attribute 3 : outward_flight_details -> Represents the Details of the Flight Outward
        - Attribute 4 : return_flight_details -> Represents the Details of the Flight Returned

    Example 1 : Flight from Frankfurt to Madrid (One_Way)
        - price : 500e
        - Operator : Lufthansa
        - outward_flight_details -> Detailed
        - return_flight_details -> None

    Example 2 :  Flight from Frankfurt to Madrid (Round Trip)
         - price : 1500e
        - Operator : Multi-Companies
        - outward_flight_details -> Detailed
        - return_flight_details -> Detailed
"""


@dataclass
class Flight:
    price: float
    operator: str
    outward_flight_details: FlightDetails
    return_flight_details: Optional[FlightDetails] = None


