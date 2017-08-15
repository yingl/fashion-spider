""" Maje """
# coding:utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['uk.maje.com']

# ul#search-result-items > li > div > div > a
def parse(driver, url):
    products = []
    driver.get(url)
    count = 0
    while True:
        driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
        util.sleep(3)
        elements = util.find_elements_by_css_selector(driver, 'ul.search-result-items > li > div > div > a')
        print(len(elements))
        if len(elements) == count:
            break
        else:
            count = len(elements)
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
