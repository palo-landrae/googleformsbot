from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Bot:
    def __init__(self, url, chrome_path, chrome_driver_path, properties):

        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path
        options.add_argument('--no-sandbox')
        # options.add_argument("--headless")
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = Service(chrome_driver_path)
        service.start()

        self.data = []
        self.url = url
        self.driver = webdriver.Chrome(service=service, options=options)
        self.properties = properties
        self.wait = WebDriverWait(self.driver, 2)
        self.last_row = 0

    def set_data(self, arr):
        self.data = arr

    def get_by_css_selector(self, selector):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            return element
        except TimeoutException:
            print(f"No such element {selector}")
            return None

    def get_by_xpath(self, xpath):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except TimeoutException:
            print(f"No such element {xpath}")
            return None

    def wait_for_page_load(self):
        try:
            self.wait.until(EC.staleness_of(
                self.driver.find_element(By.TAG_NAME, 'html')))
        except TimeoutException:
            print("Timeout waiting for page to load")

    def get_element(self, parent, selector):
        try:
            element = parent.find_element(
                By.CSS_SELECTOR, selector)
            return element
        except NoSuchElementException:
            return False

    def get_elements(self, parent, selector):
        try:
            elements = parent.find_elements(
                By.CSS_SELECTOR, selector)
            return elements
        except NoSuchElementException:
            return False

    def submit(self):
        divs_selector = 'div.Qr7Oae'
        try:
            divs = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, divs_selector)))
        except TimeoutException:
            print("Timeout occurred while waiting for elements to be present.")
            divs = []

        last_row = self.last_row
        for i, div_element in enumerate(divs[1:], start=0):
            row = i + last_row
            if self.data[row][0] == "radio":
                radio_buttons = self.get_elements(
                    div_element, "div[role='radio']")
                if radio_buttons:
                    for k, radio in enumerate(radio_buttons):
                        if k == int(self.data[row][1]):
                            radio.click()
                            self.last_row += 1
                            break

            elif self.data[row][0] == "text":
                text_field = self.get_element(
                    div_element, "input.whsOnd.zHQkBf")
                if text_field:
                    text_field.send_keys(self.data[row][1])
                    self.last_row += 1

            elif self.data[row][0] == "checkbox":
                checkboxes = self.get_elements(
                    div_element, "div[role='checkbox']")
                if checkboxes:
                    for k, checkbox in enumerate(checkboxes):
                        if k in self.data[row][1]:
                            checkbox.click()
                            self.last_row += 1
                            break

            elif self.data[row][0] == "dropdown":
                dropdown = self.get_element(div_element, "div[role='listbox']")
                if dropdown:
                    dropdown.click()
                    sleep(0.25)
                    option_selector = "div[role='option']"
                    options = div_element.find_elements(
                        By.CSS_SELECTOR, option_selector)
                    for option in options:
                        if option.text == self.data[row][1]:
                            option.click()
                            self.last_row += 1
                            break
            else:
                print("Error, element not found at row:", row)
            sleep(0.125)

    def process_page(self, skip):
        if skip:
            next_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
        else:
            if self.last_row < 48:
                self.submit()
            else:
                return True

            next_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'

        next_button = self.get_by_xpath(next_button_xpath)
        if next_button:
            # print("Moved to next page")
            next_button.click()

            sleep(1.25)
            self.process_page(False)
