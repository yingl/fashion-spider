""" Balmain """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'balmain'
PREFIXES = ['www.balmain.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div#product-panel-group > div.title')
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
    element = util.find_element_by_css_selector(driver, 'span.regular-price > span.price')
    if element:
        text = element.text.strip()[1:].replace(',', '')
    price = float(text) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.wrap_images > div > a[rel=gal1]')
    for element in elements:
        texts.append(element.get_attribute('href').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    try:
        driver.get(url)
    except:
        pass
    good = {'brand':BRAND}
    good['url'] = url
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['unit'] = 'EURO'
    good['price'] = get_price(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
