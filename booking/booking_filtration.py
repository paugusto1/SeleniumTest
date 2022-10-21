from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

    def filterByScore(self, numScore):
        print(f"*[textContent='{numScore} stars']")

        scoreRating = self.driver.find_element(by=By.CSS_SELECTOR,
                                              value=f"div[data-filters-group='review_score']")

        scores = []

        if len(numScore) == 2:
            for i in range(int(numScore[0])-1, 9, 1):
                scores.append(i+1)
        else:
            scores.append(int(numScore))

        print(scores)

        self.driver.implicitly_wait(2)
        for i in scores:
            try:
                scoreRating.find_element(by= By.XPATH, value= f"./descendant::div[contains(text(), '{i}+')]").click()
            except NoSuchElementException as e:
                print(e)

        self.driver.implicitly_wait(10)

    def sortBy(self, by):
        self.driver.find_element(by= By.XPATH, value= f"//span[contains(text(), 'Sort by')]").click()

        if by == 'popularity':
            self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value=f"button[data-id='popularity']").click()
        elif by == 'price':
            self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value=f"button[data-id='price']").click()
        elif by == 'star':
            self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value=f"button[data-id='class']").click()
        elif by == 'score':
            self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value=f"button[data-id='bayesian_review_score']").click()

        # scoreRating = self.driver.find_element(by=By.CSS_SELECTOR,
        #                                       value=f"div[data-filters-group='review_score']")
        #
        # scores = []
        #
        # if len(numScore) == 2:
        #     for i in range(int(numScore[0])-1, 9, 1):
        #         scores.append(i+1)
        # else:
        #     scores.append(int(numScore))
        #
        # print(scores)
        #
        # self.driver.implicitly_wait(2)
        # for i in scores:
        #     try:
        #         scoreRating.find_element(by= By.XPATH, value= f"./descendant::div[contains(text(), '{i}+')]").click()
        #     except NoSuchElementException as e:
        #         print(e)
        #
        # self.driver.implicitly_wait(10)


