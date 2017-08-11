""" Ysl """
# coding:utf-8

import sys
import time
sys.path.append('../')
import util

BRAND = 'ysl'
PREFIXES = ['www.yslbeautycn.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.product_name')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    # Handle subtitle
    element = util.find_element_by_css_selector(driver, 'h2.product_subtitle')
    if element:
        title += '\n' + element.text.strip()
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.price > p.product_price')
    if element:
        text = element.get_attribute('data-pricevalue').strip()
    price = float(text.replace(',', '')) if text else 0
    price = int(price)
    return price

def get_images(driver):
    images = ''
    element = util.find_element_by_css_selector(driver, 'a[data-name=product_detail_image]')
    if element:
        images = element.get_attribute('href').strip()
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
