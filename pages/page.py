from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 3

    def get_element(self, selector):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def enter_text(self, selector, text):
        input = self.get_element(selector)
        input.clear()
        input.send_keys(text)

    def click_element(self, selector):
        self.get_element(selector).click()

    def does_url_contain_path(self, path):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.url_contains(path))
            return True
        except TimeoutException:
            return False

    def get_text(self, selector):
        return self.get_element(selector).text

    def check_for_alert(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def click_link_by_text(self, text):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text))
        ).click()
