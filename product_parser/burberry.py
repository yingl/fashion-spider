""" Burberry """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'burberry'
PREFIXES = ['cn.burberry.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.product-purchase_name')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'p.product-purchase_item-number')
    if element:
        code = element.text.strip().split(' ')[-1]
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.product-purchase_price')
    if element:
        text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    return price
    
def get_intro(driver):
    intro = ''
    element = util.find_element_by_css_selector(driver, 'li[data-tab-name=Description] > div > div > p')
    if element:
        intro = element.text.strip()
    return intro
    
def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.product-carousel_item > picture > img')
    for element in elements:
        texts.append(element.get_attribute('src').strip())
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

if __name__ == '__main__':
    DRIVER = util.create_chrome_driver()
    print(parse(DRIVER, sys.argv[1]))
    DRIVER.quit()
