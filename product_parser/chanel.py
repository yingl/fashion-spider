""" Chanel """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'chanel'
PREFIXES = ['www.chanel.cn', 'www.chanel.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div.product-name > div > h1')
    if not element:
        element = util.find_element_by_css_selector(driver, 'span.fnb_pdp-subtitle')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
        title = title.replace('\n', '-')
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.product-price.priceToUpdate')
    if not element:
        element = util.find_element_by_css_selector(driver, 'p.fnb_pdp-price')
    if element:
        text = element.text.strip()[1:]
    if text.endswith('*'):
        text = text[:-1]
    text = text.replace(',', '')
    price = float(text) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.slick-track > figure > a > img')
    if not elements:
        elements = util.find_elements_by_css_selector(driver, 'div.fnb_thumbnail-img > img')
    for element in elements:
        texts.append(element.get_attribute('src').strip())
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
