""" Valentino """
# coding: utf-8

import sys
sys.path.append('../')
import util

PREFIXES = ['www.valentino.cn']

def parse(driver, url):
    products = []
    try:
        driver.get(url)
    except:
        pass
    elements = util.find_elements_by_css_selector(driver, 'article.search-item > header > a')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return ';'.join(products)

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
