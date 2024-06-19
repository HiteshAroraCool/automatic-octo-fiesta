from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os

os.environ["PATH"] += r"C:/SeleniumDrivers"
print(os.environ["PATH"])

# Opening Google
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

time.sleep(2)

# Google Search for "arcgis/rest/services"
search_bar = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
search_bar.send_keys("arcgis/rest/services")
search_bar.send_keys(Keys.RETURN)

time.sleep(2)

links = []
while len(links) <= 100:
    
    # Getting Links
    # <cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://developers.arcgis.com<span class="ylgVCe ob9lvb" role="text"> › rest › services-reference</span></cite>
    cite_elements = driver.find_elements(By.TAG_NAME, "cite")

    # Extract and print the URLs
    for element in cite_elements:
        if "arcgis" and "rest" and "services" in element.text:
            links.append(element.text)

    print("Extracted URLs:")
    for link in links:
        print(link)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, "T7sFge sW9g3e VknLRd").click()
    except:
        print("More result")
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
driver.quit()