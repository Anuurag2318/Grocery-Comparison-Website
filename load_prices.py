import sqlite3
from scripts import webscrapers as wb
conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_jiomart, url_dmart, url_bigbasket
             FROM products_product""")
database_urls = c.fetchall()
for rows in database_urls:
    for url in rows:
        if "jiomart.com" in url:
            jiomart_price = wb.jiomart_scrape(url)
            print(jiomart_price)
            c.execute("""UPDATE products_product
                         SET price_jiomart=?
                         WHERE url_jiomart=?""", (jiomart_price, url))
        elif "dmart.in" in url:
            dmart_price = wb.dmart_scrape(url)
            print(dmart_price)
            c.execute("""UPDATE products_product
                         SET price_dmart=?
                         WHERE url_dmart=?""", (dmart_price, url))
        elif "bigbasket.com" in url:
            bigbasket_price = wb.bigbasket_scrape(url)
            print(bigbasket_price)
            c.execute("""UPDATE products_product
                         SET price_bigbasket=?
                         WHERE url_bigbasket=?""", (bigbasket_price, url))
        else:
            print("FLAG: Is the following url correct? {}".format(url))
conn.commit()
c.close()
conn.close()
