import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    ls = ['Ivan', 'Petrov', 'Smolensk', 'Russia']
    selection = browser.find_elements(By.XPATH, '/html/body/div/form/div/div/input')

    for i, sel in enumerate(selection):
        sel.send_keys(ls[i])
    

    # input2 = browser.find_element(By.CSS_SELECTOR, 'form-control third')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, 'city')
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
