#coding: utf-8
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

# ChromeDriver
ChromeDriver = 'D:/LocalProject/ProjectsForFun/webCraring/chromedriver.exe'
driver = webdriver.Chrome(ChromeDriver)
driver.get('http://www.everpuresizing.com/')
print(driver.current_url)