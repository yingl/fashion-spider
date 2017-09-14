""" APM """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'apm'
PREFIXES = ['www.apm-monaco.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div.product-name > span.h5.text-uppercase')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'div.product-name > span.h6.text-uppercase')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.price')
    if element:
        text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = set([])
    elements = util.find_elements_by_css_selector(driver, 'div.fotorama__thumb > img')
    for element in elements:
        img = element.get_attribute('src').strip()
        if img.endswith('.jpg') and (not img.endswith('default.jpg')):
            texts.add(img)
    images = ';'.join(list(texts))
    return images

def parse(driver, url):
    driver.get(url)
    util.sleep(3)
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
