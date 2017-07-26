""" Miumiu """
# coding: utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['www.miumiu.com']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = util.find_elements_by_css_selector(driver, 'div.product > div > a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
