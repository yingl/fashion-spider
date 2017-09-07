""" Fendi """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'fendi'
PREFIXES = ['www.fendi.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div.content > h1')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'div.details-field.details-field-productcode > p')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    # No price for Fendi products
    price = 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.gallery-nav > div > a')
    for element in elements:
        texts.append(element.get_attribute('href').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    good = {'brand':BRAND}
    good['url'] = url
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['unit'] = 'RMB'
    good['price'] = get_price(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
