import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input_1 = browser.find_element(By.CSS_SELECTOR, 'div .first_block .form-control.first')
    input_1.send_keys('Petr')

    input_3 = browser.find_element(By.CSS_SELECTOR, 'div .first_block .form-control.third')
    input_3.send_keys('PivoVanTer@mail.org')

    input_4 = browser.find_element(By.CSS_SELECTOR, 'div .second_block .form-control.first')
    input_4.send_keys('+7 800 888 80 00')

    input_5 = browser.find_element(By.CSS_SELECTOR, 'div .second_block .form-control.second')
    input_5.send_keys('Russia, Krasnodar')

    input_2 = browser.find_element(By.CSS_SELECTOR, 'div .first_block .form-control.second')
    input_2.send_keys('Ivanov')



    # for some cases
    # xpath_for_4 = '/html/body/div/form/div[@class="second_block"]/div[@class="form-group first_class"]/input'
    # xpath_for_5 = '/html/body/div/form/div[@class="second_block"]/div[@class="form-group second_class"]/input'


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
