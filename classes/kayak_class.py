from api.utils.kayak_utils import *
from api.utils.webdriver import WebDriverClass


class KayakService:

    def __init__(self, origin, destination, outbound_date, return_date=None):
        self.origin = origin
        self.destination = destination
        self.outbound_date = outbound_date
        self.return_date = return_date
        print("Kayak Class Initialized")

    @staticmethod
    def handle_cookies_kayak(driver):
        return handle_cookie_consent(driver=driver)

    @staticmethod
    def scroll_bottom(driver):
        return scroll_to_bottom(driver=driver)

    @staticmethod
    def load_all_flights(driver):
        return click_show_more(driver=driver)

    @staticmethod
    def main_scraping_kayak(driver):
        return main_scraping_script(driver=driver)

    # Main Function to Scrap Data from [Kayak.de]
    def scrap_data(self):
        driver = WebDriverClass().get_driver()
        url = f'https://www.kayak.de/flights/{self.origin}-{self.destination}/{self.outbound_date if self.outbound_date else ""}/{self.return_date if self.return_date else ""}'
        driver.get(url)

        self.handle_cookies_kayak(driver)

        self.scroll_bottom(driver)

        # Remove Comment to Load all Flights
        # self.load_all_flights(driver)

        try:
            result = self.main_scraping_kayak(driver)
            return result
        except Exception as e:
            print(f"Error Occurred {e}")
            return {"Error": e}
        finally:
            driver.quit()
