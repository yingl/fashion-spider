""" Product spider """
# coding:utf-8

import sys
import time
import traceback
import util

_PARSERS = util.load_parsers('product_parser')

def parse(job, config):
    driver = None
    result = {'id':job['id'],
              'source_id':job['source_id'],
              'status':config.JS_FAILED,
              'content':'',
              'message':''}
    url = job['url']
    prefix = url.split('//')[1].split('/')[0]
    try:
        if prefix in _PARSERS:
            driver = util.create_chrome_driver()
            content = _PARSERS[prefix](driver, url)
            result['status'] = config.JS_FINISHED
            result['content'] = content
        else:
            raise Exception('Parser not found for %s' % url)
    except Exception as e:
            print('job %d hit exception: %s\n%s' % (job['id'], e, traceback.format_exc()))
            result['message'] = '%s\n%s' % (e, traceback.format_exc())
    finally:
        if driver:
            driver.quit()
        return result
