""" Bally """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'bally'
PREFIXES = ['www.bally.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.product-name')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text
        element = util.find_element_by_css_selector(driver, 'h2.product-short-description')
        if element:
            title += ' - ' + element.text.strip()
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'span[itemprop=price]')
    if element:
        text = element.get_attribute('content')
    price = float(text) if text else 0
    return price

def get_intro(driver):
    intro = ''
    element = util.find_element_by_css_selector(driver, 'span.js-read-more-less')
    if element:
        driver.execute_script('arguments[0].click();', element)
        util.sleep(1)
    element = util.find_element_by_css_selector(driver, 'div.js-full-content > p')
    if not element:
        element = util.find_element_by_css_selector(driver, 'div[itemprop=description] > p')
        if not element:
            element = util.find_element_by_css_selector(driver, 'div[itemprop=description]')
    if element:
        intro = element.text.strip()
    return intro

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.primary-image-item.slick-slide > a.js-producttile_link')
    for element in elements:
        texts.append(element.get_attribute('href').strip())
    images = ';'.join(texts)
    return images

def parse(driver, url):
    driver.get(url)
    good = {'brand':BRAND}
    good['title'] = get_title(driver)
    good['code'] = get_code(driver)
    good['price'] = get_price(driver)
    good['intro'] = get_intro(driver)
    good['images'] = get_images(driver)
    return good

def main():
    driver = util.create_chrome_driver()
    print(parse(driver, sys.argv[1]))
    driver.quit()

if __name__ == '__main__':
    main()
