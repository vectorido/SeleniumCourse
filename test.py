from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://github.com")
