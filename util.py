""" Util code for spider_sample """
# coding:utf-8

import importlib
import os
from selenium import webdriver

def create_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options = options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver

def find_element_by_css_selector(item, selector):
    try:
        return item.find_element_by_css_selector(selector)
    except:
        return None
        
def find_elements_by_css_selector(item, selector):
    try:
        return item.find_elements_by_css_selector(selector)
    except:
        return []

def load_parsers(folder, name=''):
    if folder.endswith('/'):
        folder = folder[:-1]
    parsers = {}
    for f in os.listdir(folder):
        if not os.path.isfile(folder + '/' + f):
            continue
        if name and (f != (name + '.py')):
            continue
        if f.endswith('.py'):
            module = importlib.import_module(folder + '.' + f[:-3])
            for prefix in module.PREFIXES:
                parsers[prefix] = module.parse
                print('Parse for %s loaded.' % prefix)
    return parsers
