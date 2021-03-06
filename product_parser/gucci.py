""" Gucci """
# coding:utf-8

import sys
import time
sys.path.append('../')
import util

BRAND = 'gucci'
PREFIXES = ['www.gucci.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.spice-product-name')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'div.spice-style-number-title > span')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.goods-price')
    if element:
        text = element.text.strip()[1:]
    price = int(text.replace(',', '')) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.spice-carsoul-wrapper > div > div > ul > li > div > div > a > img')
    for element in elements:
        texts.append(element.get_attribute('src').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    time.sleep(5) # Wait some time util everything displayed
    good = {'brand':BRAND}
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['price'] = get_price(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
