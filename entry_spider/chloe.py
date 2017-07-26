""" Chloe """
# coding: utf-8

import sys
sys.path.append('../')
import util

prefixes = ['www.chloe.cn']

def parse(driver, url):
    products = []
    driver.get(url)
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
    util.sleep(3)
    elements = util.find_elements_by_css_selector(driver, 'section.products > article.item > div > a')
    if not elements:
        elements = util.find_elements_by_css_selector(driver, 'article.product >a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
