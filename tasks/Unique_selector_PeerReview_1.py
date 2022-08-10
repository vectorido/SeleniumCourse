from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()


def complete_form(url):
    try:
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test")
        browser.find_element(By.CSS_SELECTOR, ".btn").click()
        sleep(2)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        sleep(2)
        browser.quit()


complete_form('http://suninjuly.github.io/registration2.html')