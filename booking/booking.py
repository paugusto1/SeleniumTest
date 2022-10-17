from selenium import webdriver
from selenium.webdriver.common.by import By

from booking.constants import *
from datetime import date, datetime, timedelta

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

    def search(self, place = 'Campinas', conf = [1,[0, [1,2,3,4,5,6]],1], nDays = 16):
        destinationInput = self.find_element(by=By.CSS_SELECTOR,
                                             value="*[data-component='search/destination/input-placeholder']")
        destinationInput.click()

        destinationInput.send_keys(place)

        accommodation = self.find_element(by=By.CSS_SELECTOR,
                                             value="*[data-visible = 'accommodation']")
        accommodation.click()

        option = self.find_element(by=By.CLASS_NAME,
                                             value="sb-group__field-adults")

        bttms = option.find_elements(by= By.CSS_SELECTOR, value="button[type='button']")


        bttms[0].click()
        bttms[0].click()

        for _ in range(conf[0] - 1):
            bttms[1].click()

        option = self.find_element(by=By.CLASS_NAME,
                                             value="sb-group-children")

        bttms = option.find_elements(by= By.CSS_SELECTOR, value="button[type='button']")

        bttms[0].click()
        bttms[0].click()

        for i in range(conf[1][0] - 1):
            bttms[1].click()

            option = self.find_element(by=By.CSS_SELECTOR,
                                       value="select[data-group-child-age ='%i']" % i)
            option.send_keys(conf[1][1][i])

        option = self.find_element(by=By.CLASS_NAME,
                                             value="sb-group__field-rooms")

        bttms = option.find_elements(by= By.CSS_SELECTOR, value="button[type='button']")

        bttms[0].click()
        bttms[0].click()

        for _ in range(conf[2] - 1):
            bttms[1].click()


        print(bttms)

        self.find_element(by=By.CLASS_NAME, value="b-datepicker").click()

        self.find_element(by=By.CLASS_NAME, value="bui-calendar__date--today").click()

        today = datetime.today() + timedelta(days=nDays)
        d2 = today.strftime("%Y-%m-%d")
        print("d2 =", d2)

        found = False

        self.implicitly_wait(3)

        while not found:
            try:
                self.find_element(by=By.CSS_SELECTOR, value="*[data-date='%s']" % d2).click()
                found = True
            except:
                self.find_element(by=By.CLASS_NAME, value="bui-calendar__control--next").click()

        self.implicitly_wait(10)

        self.find_element(by=By.CLASS_NAME, value="js-sb-submit-text").click()





        # groupAdults = self.find_element(by=By.CSS_SELECTOR,
        #                                      value="*[data-visible = 'accommodation']")
        #
        # destinationInput.

        #accommodation.send_keys(place)






