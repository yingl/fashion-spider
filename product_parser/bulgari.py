""" Bulgari """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'bulgari'
PREFIXES = ['www.bulgari.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h2.bul-showcase-push-model')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'span.bul-showcase-push-ref')
    if element:
        code = element.text.strip().split(' ')[-1]
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.price')
    if element:
        text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    return price
    
def get_intro(driver):
    intro = ''
    element = util.find_element_by_css_selector(driver, 'div[data-item=description] > p')
    if element:
        intro = element.text.strip()
    return intro
    
def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'ul.slideshow-showcase > li > img.bul-valign-middle-box')
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
