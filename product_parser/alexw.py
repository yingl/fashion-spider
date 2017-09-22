""" AlexanderWang """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'alexanderwang'
PREFIXES = ['www.alexanderwang.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'h1.productName > div > span.inner.modelName')
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
    text = ''
    element = util.find_element_by_css_selector(driver, 'span.value[itemprop=price]')
    if element:
        text = element.text.strip()
    price = float(text.replace(',', '')) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div#itemImages > ul.alternativeImages > li > img')
    for element in elements:
        texts.append(element.get_attribute('src').strip())
    images = ';'.join(texts)
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
