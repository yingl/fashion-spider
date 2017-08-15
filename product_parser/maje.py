""" Maje """
# coding:utf-8

import sys
import time
sys.path.append('../')
import util

BRAND = 'maje'
PREFIXES = ['uk.maje.com']

def get_title(driver):
    title = ''
    elements = util.find_elements_by_css_selector(driver, 'span.productSubname')
    if not elements:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = elements[1].text.strip()
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.price-sales.no-discount')
    if element:
        text = element.text.strip()[1:]
    else:
        element = util.find_element_by_css_selector(driver, 'span.price-sales')
        if element:
            text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    price = int(price)
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'a.zoomMain > img')
    for element in elements:
        texts.append(element.get_attribute('src').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    time.sleep(5) # Wait some time util everything displayed
    good = {'brand':BRAND}
    good['url'] = url
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
