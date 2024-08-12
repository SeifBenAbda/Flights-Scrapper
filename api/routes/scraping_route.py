from flask import Blueprint, request, jsonify
from api.services.scraping_service import ScrapService


scrapping_bp = Blueprint('scrap_flight', __name__)
scrapping_endpoint_bp = Blueprint('scrap_flight_endpoint', __name__)

@scrapping_bp.route('/scrap_flight', methods=['POST'])
def get_scrapped_flight():
    try:
        # Parses JSON data from the request body
        data = request.get_json()

        #Hard Coded Platform Selection
        selected_platform = "kayak"
        scrap_service = ScrapService(selected_platform,data)

        result = scrap_service.get_flights()
        return result
    except Exception as e:
        print(jsonify({'error': str(e)}))



"""
    Hard Coded Endpoint to Test How the Data Looks in Json Format 
    Inputs : 
        * Airport 1 : FRA (Frankfurt Germany)
        * Airport 2 : MNL (Manilla Philippines)
        * Outbound Date : 2024-06-18
        * Return Date : 2024-06-20
        
    Endpoint : /scrap_flight_endpoint
"""

@scrapping_endpoint_bp.route('/scrap_flight_endpoint', methods=['GET', 'POST'])
def get_scrapped_flight():
    try:
        # Hardcoded test data
        data = {
            "from_airport": "FRA",
            "landing_airport": "MNL",
            "date": "2024-06-24"
        }

        selected_platform = "kayak"
        scrap_service = ScrapService(selected_platform, data)
        #scrap_service.get_flights()

        return jsonify(scrap_service.get_flights())
    except Exception as e:
        return jsonify({'error': str(e)}), 500




# Route for booking
