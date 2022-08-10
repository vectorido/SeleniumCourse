from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.get(link)

    number = browser.find_element(By.CSS_SELECTOR, '.container #input_value')

    input = browser.find_element(By.CSS_SELECTOR, '.form-control')
    input.send_keys(calc(number))

    checkbox =
    radiobutton =

