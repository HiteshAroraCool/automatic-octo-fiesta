from selenium import webdriver
import os

os.environ["PATH"] += r"C:/SeleniumDrivers"
print(os.environ["PATH"])

driver = webdriver.Chrome()
driver.get('http://selenium.dev')
