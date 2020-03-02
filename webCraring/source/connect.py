#coding: utf-8
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

# ChromeDriver
driver = webdriver.Chrome()
driver.get('http://www.everpuresizing.com/')
driver.implicitly_wait(5)
print(driver.current_url)
