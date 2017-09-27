""" Valentino """
# coding: utf-8

import sys
sys.path.append('../')
import util

BRAND = 'valentino'
PREFIXES = ['www.valentino.cn']

def get_title(driver):
    title = ''
    element = util.find_element_by_css_selector(driver, 'div.item-info > h1 > div.title > span.value')
    if not element:
        raise Exception('Title not found for %s' % driver.current_url)
    else:
        title = element.text.strip()
    return title

def get_code(driver):
    code = ''
    element = util.find_element_by_css_selector(driver, 'span.inner.modelName')
    if element:
        code = element.text.strip()
    return code

def get_price(driver):
    price = 0
    text = ''
    element = util.find_element_by_css_selector(driver, 'div.item-price > div > span.price > span.value')
    if element:
        text = element.text.strip().replace(',', '')
    price = float(text) if text else 0
    return price

def get_images(driver):
    images = ''
    texts = []
    elements = util.find_elements_by_css_selector(driver, 'div.overlayElements > ul > li > img')
    for element in elements:
        # <img alt="VALENTINO GARAVANI UOMO MY0B0581RAU E41 Tote 手袋 U f" class="alternativeImageZoom" data-ytos-code10="45341239JA" data-ytos-image-shot="f" data-ytos-image-size="14_n" itemprop="image" sizes="100vw" srcset="https://media.yoox.biz/items/45/45341239ja_11_n_f.jpg 320w,https://media.yoox.biz/items/45/45341239ja_13_n_f.jpg 631w,https://media.yoox.biz/items/45/45341239ja_14_n_f.jpg 1570w">
        code = element.get_attribute('data-ytos-code10').strip().lower()
        shot = element.get_attribute('data-ytos-image-shot').strip().lower()
        size = element.get_attribute('data-ytos-image-size').strip().lower()
        texts.append('https://media.yoox.biz/items/45/' + code + '_' + size + '_' + shot + '.jpg')
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
