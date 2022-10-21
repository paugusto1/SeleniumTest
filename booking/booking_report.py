from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, driver : webdriver.Chrome):
        self.driver = driver

    def getReports(self, numResults = 10):

        results = self.driver.find_elements(by=By.CSS_SELECTOR, value="*[data-testid='property-card']")

        collection = []

        for i in results:
            name = i.find_element(by=By.CSS_SELECTOR, value="*[data-testid = 'title']").text
            address = i.find_element(by=By.CSS_SELECTOR, value="*[data-testid = 'address']").text
            score = i.find_element(by=By.CSS_SELECTOR, value="*[data-testid = 'review-score']").text.split(sep='\n')[0]

            price =  i.find_element(by=By.CSS_SELECTOR, value="*[data-testid='price-and-discounted-price']").text.split(sep=' ')

            link = i.find_element(by=By.CSS_SELECTOR, value="*[data-testid='availability-cta']").find_element(by=By.TAG_NAME, value="a").get_property("href")

            if len(price) == 2:
                price = "".join(price)
                price += "(Original price)"
            else:
                price = "".join(price)
                price += "(Original price - Price with Discount)"

            collection.append([name,address,score,price,link])
            #print(f"{name}, {address}, {score}, {price}, {link}")

            numResults -= 1

            if numResults == 0:
                break

        return collection