from selenium.webdriver.common.by import By

"""
    This Class is Responsible to Scrap Data From Kayak.de
    It Takes as Parameter the 'Root Wrapper' that has Children who hold the Data
    
    For RoundTrip Flights : 
         Main Wrapper : 'nrc6-main'
         List of Both Flights : 'hJSA-list'
         Outbound Flight : 'hJSA-item' + Indicate it by Index (1)
         Return Flight : 'hJSA-item' + Indicate it by Index (2)
"""


class KayakScrapFunc:
    def __init__(self,wrapper):
        self.wrapper = wrapper

    def get_images(self):
        wrapper = self.wrapper
        image_list = {}
        image_elements = wrapper.find_elements(By.CLASS_NAME, 'c5iUd-leg-carrier')
        index = 1
        for img_wrapper in image_elements:
            img = img_wrapper.find_element(By.TAG_NAME, 'img')
            img_source = img.get_attribute('src')
            image_list[f"Image {index}"] = img_source
            index += 1

        return image_list


    def get_prices(self):
        wrapper = self.wrapper
        prices_list = {}
        prices = wrapper.find_elements(By.CLASS_NAME, 'f8F1-price-text')
        for price in prices:
            prices_list["Price"] = price.text

        return prices_list


    def get_operator(self):
        wrapper = self.wrapper
        op_list = {}
        operators = wrapper.find_elements(By.CLASS_NAME, 'J0g6-operator-text')
        for op in operators:
            op_list["Operator"] = op.text

        return op_list


    def get_origin_and_destination_airports(self):
        wrapper = self.wrapper
        origin_dest_ap = {}
        ofa = wrapper.find_element(By.CLASS_NAME, 'EFvI')
        origin_dest_ap['Outbound_Flight_AirPorts'] = ofa.text

        return origin_dest_ap


    def get_number_stops(self):
        wrapper = self.wrapper
        num_stops_result = {}
        num_stops = wrapper.find_element(By.CLASS_NAME, 'JWEO-stops-text')
        num_stops_result["Number Stops"] = num_stops.text
        if num_stops.text != "Nonstop":
            number_stops_count = int(''.join(filter(str.isdigit, num_stops.text)))
            try:
                for index in range(1, number_stops_count + 1):
                    span_beg = wrapper.find_element(By.XPATH, f".//div[@class='c_cgF c_cgF-mod-variant-full-airport']/span[{index}]/span")
                    title_tia = span_beg.get_attribute('title')
                    num_stops_result[f"Stop {index}"] = title_tia
            except Exception as e:
                print(e)

        return  num_stops_result


    """
        Returns the Take Off And Landing Time (Including the Change Time if there is one or more)
        Returns Extra Days If the landing time isn't on the same day as the Taking off
    """

    def get_take_off_landing_time_extra_days(self):
        wrapper = self.wrapper
        result = {}
        time_container = wrapper.find_element(By.CLASS_NAME, 'vmXl.vmXl-mod-variant-large')

        # Extract the Take-Off Time (first span)
        take_off_time = time_container.find_elements(By.TAG_NAME, 'span')[0].text

        # Extract the Landing Time (last span without the sup)
        landing_time_span = time_container.find_elements(By.TAG_NAME, 'span')[2]
        try:
            sup_elements = landing_time_span.find_elements(By.TAG_NAME, 'sup')
            if sup_elements:
                flag = int(sup_elements[0].text)
                landing_time = landing_time_span.text.split('+')[0].strip()
                result['Landing Time'] = landing_time
            else:
                flag = 0
            result['Extra Days Trip'] = flag
        except Exception as e:
            print("error")
        result['Landing Time'] = landing_time_span.text
        result['Take Off Time'] = take_off_time

        return result


    """
        Returns the Flight Duration (One Way) Either Outbound or Return Flight
    """

    def get_flight_duration(self):
        wrapper = self.wrapper
        flight_duration_result = {}
        flight_duration = wrapper.find_elements(By.CLASS_NAME, 'vmXl-mod-variant-default')
        for fd in flight_duration:
            flight_duration_result['Duration'] = fd.text

        return  flight_duration_result