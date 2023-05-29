from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def dmart_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    d_price = wd.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/div/div[1]/span[2]/span')
    product_price = d_price.text
    return product_price[2:]
def jiomart_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    j_price = wd.find_element(by=By.XPATH, value='//*[@id="price_section"]/div[1]/span[1]')
    product_price = j_price.text
    return product_price[1:]

def bigbasket_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    a_price = wd.find_element(by=By.CLASS_NAME, value="IyLvo")
    product_price = a_price.text
    return product_price[3:]

