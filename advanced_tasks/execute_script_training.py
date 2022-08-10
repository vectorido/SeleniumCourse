import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    num = browser.find_element(By.ID, 'input_value')
    num = int(num.text)
    browser.execute_script("window.scrollBy(0, 100);")

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(calc(num))

    checkbox_field = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_field.click()

    radio_field = browser.find_element(By.ID, 'robotsRule')
    radio_field.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
