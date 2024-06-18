from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

os.environ["PATH"] += r":/usr/local/SeleniumDrivers"
print(os.environ["PATH"])


options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get('http://selenium.dev')
driver.quit()