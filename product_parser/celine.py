""" Celine """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'celine'
PREFIXES = ['www.celine.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'span.hd')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.split('<br>')[0].strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'span.sku')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.price > div.p > p')
    if element:
        print(element)
        print('xxx', element.text)
        text = element.text.split()[0].strip()
    price = float(text.replace('.', '')) if text else 0
    return price

def get_intro(driver):
    intro = ''
    element = util.find_element_by_css_selector(driver, 'span.hd')
    if element:
        texts = []
        for text_ in element.text.split('<br>'):
            texts.append(text_.strip())
        intro = '\n'.join(texts)
    return intro
    
def get_images(driver):
    images = ''
    element = util.find_element_by_css_selector(driver, 'span.cycle-slide-active > img')
    if element:
        images = element.get_attribute('data-src-zoom').strip()
    return images

def parse(driver, url):
    driver.get(url)
    util.sleep(5) # Wait some time util everything displayed
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
