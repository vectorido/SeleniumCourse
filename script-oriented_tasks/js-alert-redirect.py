import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Firefox()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    num = browser.find_element(By.CSS_SELECTOR, '#input_value')
    num = int(num.text)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(calc(num))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
