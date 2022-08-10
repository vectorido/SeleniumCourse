from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Firefox()
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1')
    num_2 = browser.find_element(By.ID, 'num2')

    required = str(int(num_1.text) + int(num_2.text))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(required)  # ищем элемент с текстом "Python"


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()