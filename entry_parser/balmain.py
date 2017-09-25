""" Balmain """
# coding:utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['www.balmain.com']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = []
    count = -1
    while len(elements) > count:
        count = len(elements)
        driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
        util.sleep(2)
        elements = util.find_elements_by_css_selector(driver, 'div.products-list > div > a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
