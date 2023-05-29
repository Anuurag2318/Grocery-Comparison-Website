import sqlite3
# from scripts import webscrapers as wb
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_jiomart FROM products_product""")
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
def jiomart_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    j_price = wd.find_element(by=By.XPATH, value='//*[@id="price_section"]/div[1]/span[1]')
    product_price = j_price.text
    return product_price[1:]
for rows in database_urls:
    for url in rows:
        if "jiomart.com" in url:
            jiomart_price = jiomart_scrape(url)
            print(jiomart_price)
            c.execute("""UPDATE products_product
                         SET price_jiomart=?
                         WHERE url_jiomart=?""", (jiomart_price, url))
        else:
            print("FLAG: Is the following url correct? {}".format(url))


# print(jiomart_scrape('https://www.jiomart.com/p/groceries/tata-iodised-salt-1-kg/490000073'))
conn.commit()
c.close()
conn.close()