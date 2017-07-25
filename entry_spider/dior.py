""" Dior """
# coding: utf-8

import sys
sys.path.append('../')
import util

prefixes = ['www.dior.cn']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = util.find_elements_by_css_selector(driver, 'div.product > div > div > a')
    if not elements:
        elements = util.find_elements_by_css_selector(driver, 'div.column > div.push-pic > a')
        if not elements:
            elements = util.find_elements_by_css_selector(driver, '[id|=push-produit] > div > div > a')
            if not elements:
                 elements = util.find_elements_by_css_selector(driver, 'span.univers-part--product > div > div > a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

if __name__ == '__main__':
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()
