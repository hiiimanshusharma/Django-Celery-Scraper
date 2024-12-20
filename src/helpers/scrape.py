from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()
options.add_argument('--headless')

def fetch_html(url):
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        time.sleep(3)
        html = driver.page_source

    return html