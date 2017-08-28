""" AcneStudios """
# coding:utf-8

import sys
import time
sys.path.append('../')
import util

BRAND = 'acnestudios'
PREFIXES = ['www.acnestudios.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div.product-name')
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
    element = util.find_element_by_css_selector(driver, 'div.product-item__detail-price > div > span')
    if element:
        text = element.text.strip()[1:]
    price = float(text.replace(',', '')) if text else 0
    price = int(price)
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.product-item__gallery-item-image > a > img')
    for element in elements:
        texts.append(PREFIXES[0] + element.get_attribute('data-zoom-src').strip())
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
