""" Versace """
# coding: utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['www.versace.cn']

def parse(driver, url):
    products = []
    driver.get(url)
    for i in range(10):
        driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
        util.sleep(1)
    elements = util.find_elements_by_css_selector(driver, 'div.js-product-image > a.js-producttile_link')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
