import sqlite3
# from scripts import webscrapers as wb
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_dmart FROM products_product""")
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
PATH="C:\chromedriver_win32\chromedriver.exe"
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
database_urls = c.fetchall()
def dmart_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    d_price = wd.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/div/div[1]/span[2]/span')
    product_price = d_price.text
    return product_price[2:]
for rows in database_urls:
    for url in rows:
        if "dmart.in" in url:
            dmart_price = dmart_scrape(url)
            print(dmart_price)
            c.execute("""UPDATE products_product
                         SET price_dmart=?
                         WHERE url_dmart=?""", (dmart_price, url))
conn.commit()
c.close()
conn.close()