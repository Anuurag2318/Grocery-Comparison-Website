import sqlite3
# from scripts import webscrapers as wb
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_bigbasket FROM products_product""")
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
def bigbasket_scrape(url):
    wd.get(url)
    wd.implicitly_wait(wait_imp)
    a_price = wd.find_element(by=By.CLASS_NAME, value="IyLvo")
    product_price = a_price.text
    return product_price[3:]
for rows in database_urls:
    for url in rows:
        if "bigbasket.com" in url:
            bigbasket_price = bigbasket_scrape(url)
            print(bigbasket_price)
            c.execute("""UPDATE products_product
                         SET price_bigbasket=?
                         WHERE url_bigbasket=?""", (bigbasket_price, url))
        else:
            print("FLAG: Is the following url correct? {}".format(url))

conn.commit()
c.close()
conn.close()



