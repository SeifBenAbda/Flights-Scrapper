from api.utils.common_imports_kayak import *
from api.utils.kayak_scrap_func import KayakScrapFunc

# This Function Bypass Cookies on the Platform Kayak.de
def handle_cookie_consent(driver):
    try:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@class='RxNS RxNS-mod-stretch RxNS-mod-variant-outline RxNS-mod-theme-base RxNS-mod-shape-default RxNS-mod-spacing-base RxNS-mod-size-small']"))
        )

        # Click the button
        button.click()
        print("Cookie consent button clicked successfully!")
    except TimeoutException:
        print("Timed out waiting for the cookie consent button to be clickable.")
    except Exception as e:
        print(f"Error: {e}")


# This function Scrolls to the Bottom of Platform
def scroll_to_bottom(driver):
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for scrolling to finish


# This Function keep loading all Flights on [Kayak.de] until the "Show More" Button disappears from DOM
def click_show_more(driver):
    while True:
        try:
            # Check if the "Show More" button exists
            show_more_button = driver.find_element(By.CLASS_NAME, 'ULvh-button.show-more-button')

            # Click the "Show More" button
            show_more_button.click()

            # Wait for a short time to allow new results to load
            time.sleep(2)

        except NoSuchElementException:
            # If the "Show More" button is not found, exit the loop
            break

        except Exception as e:
            print(f"Error: {e}")
            break

# Locate Main Wrapper
def main_scraping_script(driver):
    flight_results = []
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'nrc6-wrapper'))
    )
    wrapper_elements = driver.find_elements(By.CLASS_NAME, 'nrc6-wrapper')

    # Use ThreadPoolExecutor for parallel data fetching
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(scrap_details, wrapper_elements)

    flight_results = list(results)

    return flight_results



# Main Script
# Returns Json of ['origin_airport' , 'landing_airport' , 'extra_days' , 'take_off_time' , 'landing_time' , 'duration' , 'operator' , 'images']
def scrap_details(wrapper):
    kayak_func = KayakScrapFunc(wrapper)
    main_flights_wrapper = wrapper.find_elements(By.CLASS_NAME, 'hJSA-list')
    all_flights_data = {}

    try:
        single_flight_data = {}

        #Prices + Operator are Global :
        single_flight_data.update(kayak_func.get_prices())
        single_flight_data.update(kayak_func.get_operator())


        #Details Wrapper 'hJSA-list'
        for item in main_flights_wrapper:
            wrapper_details = wrapper.find_elements(By.CLASS_NAME, 'hJSA-item')

            #Index of Flight Details (Max Index 2) : Index 1 -> Outbound Flight / Index 2 -> Return Flight
            index = 1
            for flight_detail in wrapper_details:
                kayak_func_details = KayakScrapFunc(flight_detail)
                main_flight_details = {}

                #Origin and Destination Airports
                main_flight_details.update(kayak_func_details.get_origin_and_destination_airports())

                #Number of Stops
                main_flight_details.update(kayak_func_details.get_number_stops())

                # Images For Single Flight
                main_flight_details.update(kayak_func_details.get_images())

                #Take-Off + Landing Time + Extra Days In Between
                main_flight_details.update(kayak_func_details.get_take_off_landing_time_extra_days())

                #Flight Duration
                main_flight_details.update(kayak_func_details.get_flight_duration())

                single_flight_data.update({f"Flight Details {index}": main_flight_details})
                index +=1



        all_flights_data.update(single_flight_data)



    except Exception as e:
        print(f"Error: {e}")
    return all_flights_data