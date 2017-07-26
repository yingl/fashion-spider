""" Cartier """
# coding: utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['www.cartier.cn']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = util.find_elements_by_css_selector(driver, 'a.prod-link')
    if elements:
        for element in elements:
            if element.get_attribute('style') != 'display: none;':
                products.append(element.get_attribute('href').strip())
    else:
        elements = util.find_elements_by_css_selector(driver, 'div.comp-rich-text > p > a')
        for i in range(len(elements) - 1):
            products.append(elements[i].get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
