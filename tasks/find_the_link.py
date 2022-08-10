import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_link_text'
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    # step_1

    browser = webdriver.Firefox()
    browser.get(link)
    input_x = browser.find_element(By.LINK_TEXT, text)
    input_x.click()

    # step_2

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    browser.quit()
