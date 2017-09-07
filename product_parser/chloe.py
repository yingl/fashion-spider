""" Chloe """
# coding:utf-8

import sys
sys.path.append('../')
import util

BRAND = 'chloe'
PREFIXES = ['www.chloe.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'span.inner.modelName')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
        element = util.find_element_by_css_selector(driver, 'div.composition > p > span.value')
        if element:
            title += ('-' + element.text.strip())
    return title

def get_code(driver):
    return ''

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.itemBoxPrice > div.priceUpdater > span.price > span.value')
    print(element)
    if element:
        text = element.text.strip()
        print(text)
    price = float(text.replace(',', '')) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'ul.alternativeImages > li > img')
    for element in elements:
        data = element.get_attribute('srcset')
        texts.append(data.split(' ')[0])
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
