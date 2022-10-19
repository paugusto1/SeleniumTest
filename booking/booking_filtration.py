from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver : webdriver.Chrome):
        self.driver = driver

    def filterByStar(self, numStar = None):
        print(f"*[textContent='{numStar} stars']")

        starRating = self.driver.find_element(by=By.CSS_SELECTOR,
                                              value=f"div[data-filters-group='class']")

        if numStar is None:
            starRating.find_element(by=By.XPATH, value=f"//*[text()='Unrated']").click()
        else:

            stars = []

            if len(numStar) == 2:
                for i in range(int(numStar[0])-1, 5, 1):
                    stars.append(i+1)
            else:
                stars.append(int(numStar))

            print(stars)

            self.driver.implicitly_wait(2)
            for i in stars:
                star = 'star' if i == 1 else 'stars'
                try:
                    starRating.find_element(by= By.XPATH, value= f"./descendant::div[text()='{i} {star}']").click()
                except NoSuchElementException as e:
                    print(e)


            self.driver.implicitly_wait(10)

