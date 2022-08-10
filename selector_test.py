from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    print(button.text)

finally:
    browser.quit()
