import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchScraper:
    def __init__(self, query):
        self.query = query
        self.driver = self.initialize_driver()
        self.URL_links = []
        self.path_to_csv = "links.csv"

    def initialize_driver(self):
        os.environ["PATH"] += r"C:/SeleniumDrivers"
        driver = webdriver.Chrome()
        return driver

    def open_google(self):
        self.driver.get('https://www.google.com/')
        time.sleep(1)

    def perform_search(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, '[name="q"]')
        search_bar.send_keys(self.query)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(1)

    def scrape_links(self):
        while True:
            try:
                 #<a class="T7sFge sW9g3e VknLRd __web-inspector-hide-shortcut__" href="/search?q=google&amp;sca_esv=453f36eb1da0db3c&amp;sca_upv=1&amp;sxsrf=ADLYWILpCMZphdwloOSongsix67lh9jpHw:1718887947976&amp;ei=CyZ0ZrCBO9jZseMP3tWk0Ag&amp;start=10&amp;sa=N" style="transform: scale(1);" jsname="oHxHid" jsaction="qBEZuc" aria-label="More results" data-ve-view="" role="button" data-hveid="CAkQBA" data-ved="2ahUKEwjwsrDMnOqGAxXYbGwGHd4qCYoQqq4CegQICRAE" aria-hidden="false"><hr class="KXbwLb" aria-hidden="true"><h3 aria-hidden="true"><div class="GNJvt ipz2Oe"><span class="kQdGHd"><span class="OTvAmd z1asCe QFl0Ff"><svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></span></span><span class="RVQdVd">More results</span></div></h3></a>
                # https://www.google.com/search?q=arcgis/rest/services&sca_esv=453f36eb1da0db3c&sca_upv=1&source=hp&ei=9Sl0ZsXsNoTX1e8PwtyZ8AM&iflsig=AL9hbdgAAAAAZnQ4BcOeJKbZ3lqqsvA6Y5TnrBOluZWK&uact=5&oq=arcgis/rest/services&gs_lp=Egdnd3Mtd2l6IhRhcmNnaXMvcmVzdC9zZXJ2aWNlc0hYUABYM3AAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwCgBwA&sclient=gws-wiz&aomd=1
                # Locate the "More results" link element by text
                self.driver.find_element(By.XPATH, '//a[@aria-label="More results"]').click()
                print("More results clicked")
            except:
                print("Scrolling down")
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            
            try:
                page_end = '//i[contains(text(), "In order to show you the most relevant results, we have omitted some entries very similar to the 160 already displayed.")]'
                if self.driver.find_element(By.XPATH, page_end):
                    print("Exiting loop")
                    break
            except:
                continue

        cite_elements = self.driver.find_elements(By.TAG_NAME, "cite")
        for element in cite_elements:
            if "arcgis" in element.text and "rest" in element.text and "services" in element.text:
                self.URL_links.append(element.text)

    def save_to_csv(self):
        links_dict = {
            "id": range(len(self.URL_links)),
            "link": self.URL_links
        }
        links_df = pd.DataFrame(data=links_dict)
        links_df.to_csv(self.path_to_csv, index=False)

    def run(self):
        try:
            self.open_google()
            self.perform_search()
            self.scrape_links()
            self.save_to_csv()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    scraper = GoogleSearchScraper("arcgis/rest/services")
    scraper.run()
