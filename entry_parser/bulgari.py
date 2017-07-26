""" Bulgari """
# coding: utf-8

import sys
import time
sys.path.append('../')
import util

PREFIXES = ['www.bulgari.com']

def parse(driver, url):
    products = []
    driver.get(url)
    i = 0
    while True:
        elements = util.find_elements_by_css_selector(driver, 'a.bul-btn-more')
        cont = False
        for element in elements:
            if element.is_displayed():
                cont = True
                driver.execute_script('arguments[0].click();', element)
                i += 1 # Give up after 20 times, there is bug in the page.
                if i >= 20:
                    cont = False
                    break
                time.sleep(1)
        if not cont:
            break
    elements = util.find_elements_by_css_selector(driver, 'a.product-link')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
