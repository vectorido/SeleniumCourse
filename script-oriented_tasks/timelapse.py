import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Firefox()
    browser.get(link)
    browser.implicitly_wait(15)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    num = browser.find_element(By.ID, 'input_value')
    num = int(num.text)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(calc(num))

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
