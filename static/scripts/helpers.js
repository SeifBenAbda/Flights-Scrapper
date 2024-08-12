window.onload = mainFunctions;

function mainFunctions() {
    calculateRemainingHeight()
    togglePlatform()
}


function getLoadingDivs(numLoadingElements) {
    // Get the loading element template
    var loadingElementTemplate = $('.loader');

// Clone the loading element template and append clones to #loading-content
    for (var i = 0; i < numLoadingElements; i++) {
        var clone = loadingElementTemplate.clone()
        $('#loading-content').append(clone);
    }
}

function calculateRemainingHeight() {
    // Get total screen height
    var totalHeight = window.innerHeight;

    // Get height of content above flight_results
    var contentAboveHeight = document.querySelector('.bg-grey').offsetHeight; // Adjust the selector if needed

    // Calculate remaining height
    var remainingHeight = totalHeight - contentAboveHeight;

    // Log or use remainingHeight as needed
    console.log("Remaining height for flight results: " + remainingHeight + "px");


    // Calculate number of loading elements based on remaining height
    var numLoadingElements = Math.floor(remainingHeight / 150); // Adjust 20 to your desired element height

    // Make an AJAX request to update the content of flightResultsContainer

    getLoadingDivs(numLoadingElements);
}


function togglePlatform() {
    document.querySelectorAll('[id^="box"]').forEach(box => {
        box.addEventListener('dblclick', () => {
            console.log("Hey Toggle");
            const img = box.querySelector('img');
            if (img.style.display === 'none') {
                img.style.display = 'block';
            } else {
                img.style.display = 'none';
            }
        });

        // Handle touch events for mobile devices
        box.addEventListener('touchend', () => {
            const img = box.querySelector('img');
            if (img.style.display === 'none') {
                img.style.display = 'block';
            } else {
                img.style.display = 'none';
            }
        });
    });


}

