document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('searchButton').addEventListener('click', fetch_data);
});

function showHideLoader(isShow) {
    document.getElementById('loading-content').style.display = isShow ? 'block' : 'none';
    var loadingElements = document.querySelectorAll('.loader');
    loadingElements.forEach(function (element) {
        element.style.display = isShow ? 'block' : 'none';
    });
    document.getElementById('result').style.display = isShow ? 'none' : 'block';
}


function fetch_data(event) {
    event.preventDefault(); // Prevents the form from submitting normally

    showHideLoader(true);

    // Get the search term
    const airport_from = document.getElementById('from').value;
    const airport_to = document.getElementById('to').value;

    //Missing Dates and Platform Selection


    // Make an HTTP request to your FastAPI endpoint
    fetch('http://localhost:5000/scrap_flight', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({from_airport: airport_from, landing_airport: airport_to})
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response data
            showHideLoader(false);
            updateResults(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            showHideLoader(false);
            // Handle error display if needed
        });

}

function updateResults(data) {
    const resultContainer = document.getElementById('result');
    const resultMessage = document.getElementById('result-message');
    const resultFlights = document.getElementById('result-flights');

    if (data && data.length > 0) {
        resultMessage.innerText = `Found ${data.length} flights.`;
        resultFlights.innerHTML = ''; // Clear previous results if needed

        data.forEach(flight => {
            const flightDiv = document.createElement('div');
            flightDiv.classList.add('p-4', 'bg-white', 'rounded-lg', 'shadow-md', 'mb-4');
            flightDiv.innerHTML = `
                        <div class="flex items-center">
                            <img src="${flight.outward_flight_details.operator_images}" alt="Operator Logo" class="w-16 h-16 mr-4">
                            <div>
                                <h2 class="text-xl font-semibold">${flight.operator}</h2>
                                <p class="text-lg font-bold text-red-500">${flight.price}</p>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold">Outward Flight</h3>
                            <p>${flight.outward_flight_details.airport_start} to ${flight.outward_flight_details.airport_destination}</p>
                            <p>${flight.outward_flight_details.take_off_time} - ${flight.outward_flight_details.landing_time}</p>
                            <p>${flight.outward_flight_details.duration}</p>
                            <p>${flight.outward_flight_details.number_stops}</p>
                        </div>
                        ${flight.return_flight_details ? `
                        <div class="mt-4">
                            <h3 class="text-lg font-semibold">Return Flight</h3>
                            <p>${flight.return_flight_details.airport_start} to ${flight.return_flight_details.airport_destination}</p>
                            <p>${flight.return_flight_details.take_off_time} - ${flight.return_flight_details.landing_time}</p>
                            <p>${flight.return_flight_details.duration}</p>
                            <p>${flight.return_flight_details.number_stops}</p>
                        </div>` : ''}
                    `;
            resultFlights.appendChild(flightDiv);
        });

        resultContainer.style.display = 'block';
    } else {
        resultMessage.innerText = 'No flights found.';
        resultContainer.style.display = 'none';
    }
}


