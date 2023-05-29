from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import sqlite3
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
PATH="C:\chromedriver_win32\chromedriver.exe"
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def jiomart_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    j_price = wd.find_element(by=By.XPATH, value='//*[@id="price_section"]/div[1]/span[1]')
    # j_price = wd.find_element(by=By.CLASS_NAME, value='jm-heading-xs jm-ml-xxs')
    product_price = j_price.text
    return product_price
print(jiomart_scrape('https://www.jiomart.com/p/groceries/super-sarvottam-rice-bran-oil-1-l-pouch/491504124'))
