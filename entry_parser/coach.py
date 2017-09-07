""" Coach """
# coding: utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['china.coach.com']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = util.find_elements_by_css_selector(driver, 'dt > a#product_detail_a')
    for element in elements:
        products.append('http://china.coach.com' + element.get_attribute('name').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
