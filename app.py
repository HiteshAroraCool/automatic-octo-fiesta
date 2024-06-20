from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os
import pandas as pd
import regex as r
import csv

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

URL_links = []
while len(URL_links) <= 100:
    
    # Getting URL_links
    # <cite class="qLRx3b tjvcx GvPZzd cHaqb" role="text">https://developers.arcgis.com<span class="ylgVCe ob9lvb" role="text"> › rest › services-reference</span></cite>
    cite_elements = driver.find_elements(By.TAG_NAME, "cite")

    # Extract and print the URLs
    for element in cite_elements:
        if "arcgis" and "rest" and "services" in element.text:
            URL_links.append(element.text)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    try:
        #<a class="T7sFge sW9g3e VknLRd __web-inspector-hide-shortcut__" href="/search?q=google&amp;sca_esv=453f36eb1da0db3c&amp;sca_upv=1&amp;sxsrf=ADLYWILpCMZphdwloOSongsix67lh9jpHw:1718887947976&amp;ei=CyZ0ZrCBO9jZseMP3tWk0Ag&amp;start=10&amp;sa=N" style="transform: scale(1);" jsname="oHxHid" jsaction="qBEZuc" aria-label="More results" data-ve-view="" role="button" data-hveid="CAkQBA" data-ved="2ahUKEwjwsrDMnOqGAxXYbGwGHd4qCYoQqq4CegQICRAE" aria-hidden="false"><hr class="KXbwLb" aria-hidden="true"><h3 aria-hidden="true"><div class="GNJvt ipz2Oe"><span class="kQdGHd"><span class="OTvAmd z1asCe QFl0Ff"><svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></span></span><span class="RVQdVd">More results</span></div></h3></a>
        # https://www.google.com/search?q=arcgis/rest/services&sca_esv=453f36eb1da0db3c&sca_upv=1&source=hp&ei=9Sl0ZsXsNoTX1e8PwtyZ8AM&iflsig=AL9hbdgAAAAAZnQ4BcOeJKbZ3lqqsvA6Y5TnrBOluZWK&uact=5&oq=arcgis/rest/services&gs_lp=Egdnd3Mtd2l6IhRhcmNnaXMvcmVzdC9zZXJ2aWNlc0hYUABYM3AAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwCgBwA&sclient=gws-wiz&aomd=1
        
        # Locate the "More results" link element by text
        driver.find_element(By.XPATH, '//a[@aria-label="More results"]').click()
        print("More result")

    except:
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
driver.quit()

# Initialize the dictionary with empty lists for columns
links = {
    "id": range(0,len(URL_links)),
    "link": URL_links,
}

links_df = pd.DataFrame(data=links)

# Save the DataFrame to a CSV file
links_df.to_csv("links.csv", index=False)