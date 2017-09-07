""" JimmyChoo """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'jimmychoo'
PREFIXES = ['row.jimmychoo.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.product-name')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    return code

def get_price(driver):
    price = 0
    unit = 'RMB'
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.product-content > div > div.product-price > span[itemprop=price]')
    if element:
        text = element.text.strip()
    if text.find('$') >= 0:
        unit = 'USD'
        text = text.replace('$', '')
    elif text.find('€') >= 0:
        unit = 'EURO'
        text = text.replace('€', '')
    price = float(text.replace(',', '')) if text else 0
    return unit, price

def get_images(driver):
    images = ''
    texts = set([])
    elements = util.find_elements_by_css_selector(driver, 'div.js-big-images-list > div > div > div > a > img')
    for element in elements:
        texts.add(element.get_attribute('src').strip())
    images = ';'.join(list(texts))
    return images

def parse(driver, url):
    driver.get(url)
    good = {'brand':BRAND}
    good['url'] = url
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['unit'], good['price'] = get_price(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
