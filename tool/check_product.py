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
                        help='Specify the brand you want to check',
                        default='')
    return parser.parse_args()

def write_to_file(file, lines):
    with open(file, 'w+') as f:
        for line in lines:
            if line:
                f.write(line + '\n')

def main(args):
    brand = args.brand
    print(brand)
    codes = []
    prices = []
    intros = []
    images = []
    dd.init_database(pc.DB)
    source_query = dd.Source.select(dd.Source.id, dd.Source.url)
    if brand:
        source_query = source_query.where(dd.Source.url.contains('%%' + brand))
    source_query = source_query.alias('source_query')
    query = dd.Result.select(dd.Result, source_query.c.url).join(source_query, on=(source_query.c.id == dd.Result.source_id))
    print(query)
    for r in query:
        url = r.url
        print(url)
        content = eval(r.content)
        if not content['code']:
            codes.append(url)
        if not content['price']:
            prices.append(url)
        if not content['intro']:
            intros.append(url)
        if not content['images']:
            images.append(url)
    write_to_file('codes.txt', codes)
    write_to_file('prices.txt', prices)
    write_to_file('intros.txt', intros)
    write_to_file('images.txt', images)

if __name__ == '__main__':
    main(parse_args())
