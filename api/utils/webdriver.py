from selenium import webdriver

class WebDriverClass:
    def __init__(self):
        #gecko_driver_path = 'path/to/geckodriver'  # Specify the path to your GeckoDriver executable

        self.options = webdriver.FirefoxOptions()
        self.options.headless= False  # Run Firefox in headless mode

    def get_driver(self):
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=self.options,
            keep_alive=False
        )
        return driver