import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import time

def setup(dirDrivers):
    os.environ['PATH'] += dirDrivers
    print(os.environ['PATH'])
    driver = webdriver.Chrome()
    return driver

def firstTest(driver):

    driver.get(url='https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
    driver.implicitly_wait(30)

    downloadBtm = driver.find_element(by=By.ID, value="downloadButton")
    print(downloadBtm.text)
    downloadBtm.click()

    result = driver.find_element(by=By.CLASS_NAME, value="progress-label")

    count = 0

    while result.text != 'Complete!' and count != 20:
        time.sleep(1)
        count += 1

    print("Completed after %i seconds" % count)

    driver.find_element(By.XPATH, "//*[text()='Close']").click()

    downloadBtm.click()

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'progress-label'),
            'Complete!'
        )
    )


def secondTest(driver : selenium.webdriver.chrome.webdriver.WebDriver):
    """
    :type driver: webdriver.Chrome()
    """
    driver.get(url='https://demo.seleniumeasy.com/basic-first-form-demo.html')
    driver.implicitly_wait(30)

    input1 = driver.find_element(by=By.ID, value="sum1")
    input2 = driver.find_element(by=By.ID, value="sum2")
    
    input1.send_keys(15)
    input2.send_keys('8')
    result = driver.find_element(by=By.XPATH, value="//*[text() = 'Get Total']")
    
    result.click()
    input1.clear()
    input2.clear()
    input1.send_keys(15)
    input2.send_keys('15')
    result = driver.find_element(by=By.CSS_SELECTOR, value="button[onclick='return total()']")

    result.click()

    assert('30' == driver.find_element(by=By.ID, value="displayvalue").text)



d = setup(r';C:\Users\pedrov\Desktop\Programs\SeleniumDrivers')
#firstTest(d)
secondTest(d)

#input1 = d.find_element(by=By.ID, value="sum1")
#input1.clear()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
