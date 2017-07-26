""" Burberry """
# coding: utf-8

import sys

sys.path.append('../')
import util

prefixes = ['cn.burberry.com']

def parse(driver, url):
    products = []
    driver.get(url)
    elements = util.find_elements_by_css_selector(driver, 'a.shelf_view-all')
    for element in elements:
        if element.is_displayed():
            driver.execute_script('arguments[0].click();', element)
            util.sleep(3)
    elements = util.find_elements_by_css_selector(driver, 'li.product > div > a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
