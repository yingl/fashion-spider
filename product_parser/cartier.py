""" Cartier """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'cartier'
PREFIXES = ['www.cartier.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'span.c-pdp__cta-section--product-title')
    if not element:
        element = util.find_element_by_css_selector(driver, 'span.productNameBSE')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'div.c-pdp__cta-section--product-ref-id > span')
    if not element:
        element = util.find_element_by_css_selector(driver, 'span[itemprop=productID]')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.price.js-product-price-formatted')
    if not element:
        element = util.find_element_by_css_selector(driver, 'div.product-price')
    if element:
        text = element.text.strip()[1:]
    text = text.split(' ')[0]
    price = float(text.replace(',', '')) if text else 0
    return price

def get_intro(driver):
    intro = ''
    element = util.find_element_by_css_selector(driver, 'div.c-pdp__char--content > span')
    if element:
        intro = element.text.strip()
    else:
        elements = util.find_elements_by_css_selector(driver, 'span[itemprop=description]')
        if elements:
            texts = []
            for element in elements:
                texts.append(element.text.strip())
            intro = '\n'.join(texts)
    return intro

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.c-pdp__carousel-images > div > img.visible-lg')
    if elements:
        for element in elements:
            texts.append(element.get_attribute('src').strip())
    else:
        elements = util.find_elements_by_css_selector(driver, 'div[itemprop=image] > div')
        for element in elements:
            texts.append(element.get_attribute('data-original-url').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    good = {'brand':BRAND}
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['price'] = get_price(driver)
    good['intro'] = get_intro(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
