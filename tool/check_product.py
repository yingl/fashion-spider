""" Check result to find out what's missing """
# coding:utf-8

import argparse
import sys
sys.path.append('../')
import product_config as pc
import ds_database as dd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b',
                        '--brand',
                        help='Specify the brand you want to check')
    return parser.parse_args()

def write_to_file(file, lines):
    """ Write result lines to file """
    with open(file, 'w+') as f:
        for line in lines:
            if line:
                f.write(line + '\n')

if __name__ == '__main__':
    ARGS = parse_args()
    BRAND = ARGS.brand
    EMPTY_CODE = []
    EMPTY_PRICE = []
    EMPTY_INTRO = []
    EMPTY_IMAGES = []
    dd.init_database(pc.DB)
    jq = dd.Source.select(dd.Source.id, dd.Source.url)
    if BRAND:
        JOB_QUEUE = jq.where(dd.Source.url.contains('%%' + BRAND))
    JQ = JOB_QUEUE.alias('jq')
    QUERY = dd.Result.select(dd.Result, JQ.c.url).join(JQ, on=(JQ.c.id == dd.Result.source_id))
    for r in QUERY:
        url = r.url
        content = eval(r.content)
        if not content['code']:
            EMPTY_CODE.append(url)
        if not content['price']:
            EMPTY_PRICE.append(url)
        if not content['intro']:
            EMPTY_INTRO.append(url)
        if not content['images']:
            EMPTY_IMAGES.append(url)
    write_to_file('code.txt', EMPTY_CODE)
    write_to_file('price.txt', EMPTY_PRICE)
    write_to_file('intro.txt', EMPTY_INTRO)
    write_to_file('images.txt', EMPTY_IMAGES)
