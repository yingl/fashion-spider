""" Coach """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'coach'
PREFIXES = ['china.coach.com']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1#curr_skuName')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'p.pronumber')
    if element:
        code = element.text.strip().split(':')[-1]
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'input#skuPrices')
    if element:
        text = element.text.strip()
    price = float(text.replace(',', '')) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    # Main image first
    element = util.find_element_by_css_selector(driver, 'a#product_main_image > img')
    if not element:
        raise Exception('Main image not found for %s' % driver.current_url)
    else:
        texts.append(element.get_attribute('src').strip())
    elements = util.find_elements_by_css_selector(driver, 'li > a > img.lazyimg')
    for element in elements:
        img = element.get_attribute('lazy_src').strip()
        texts.append(img.replace('pd_altsq', 'pd_main'))
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
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
