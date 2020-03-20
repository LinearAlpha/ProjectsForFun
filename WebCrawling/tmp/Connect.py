#coding: utf-8
from selenium import webdriver

# ChromeDriver
driver = webdriver.Chrome()
driver.get('http://www.everpuresizing.com/')
driver.implicitly_wait(5)
print(driver.current_url)