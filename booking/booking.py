from selenium import webdriver
from selenium.webdriver.common.by import By

from booking.constants import *
import os

class Booking(webdriver.Chrome):

    def __init__(self, driverpath = DRIVERS_PATH, teardown = False):
        self.driver_path = driverpath
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def change_currency(self, curr = 'BRL'):
        self.find_element(by=By.CSS_SELECTOR, value="button[data-modal-header-async-type='currencyDesktop']").click()
        self.find_element(by=By.CSS_SELECTOR, value="a[data-modal-header-async-url-param*='%s']" % curr).click()



