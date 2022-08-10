import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# you can also use absolute path of your file
# current_dir = '/'

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)

    data = ['Charles', 'Bankings', 'cba@agency.gov']

    inputs = browser.find_elements(By.CLASS_NAME, 'form-control')
    for i, input in enumerate(inputs):
        input.send_keys(data[i])

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'resume.txt')
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
