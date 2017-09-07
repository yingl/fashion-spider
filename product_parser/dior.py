""" Dior """
# coding:utf-8

import sys
import time
sys.path.append('../')
import util

BRAND = 'dior'
PREFIXES = ['www.dior.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.quickbuy-title')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.quickbuy-details > span.details-price')
    if element:
        text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    price = int(price)
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'ul.cover-thumbnails.js-cover-thumbs > li > a')
    for element in elements:
        data = element.get_attribute('data-zoom')
        if not data:
            element = util.find_element_by_css_selector(element, 'img')
            if element:
                data = element.get_attribute('data-zoom')
        text = 'https://www.dior.cn' + eval(data)['src'].replace('\\', '')
        texts.append(text)
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    time.sleep(5) # Wait some time util everything displayed
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
