""" Fetch product urls from entry's result table """
# coding:utf-8

import argparse
import sys
sys.path.append('../')
import ds_database as dd
import entry_config as ec

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b',
                        '--brand',
                        help='Specify the brand you want to fetch',
                        default='')
    return parser.parse_args()

def main(args):
    brand = args.brand
    dd.init_database(ec.DB)
    rows = dd.Result.select()
    if brand:
        rows = rows.where(dd.Result.content.contains(brand))
    urls = set([])
    prodct_count = 0
    for row in rows:
        for product in row.content.split(';'):
            prodct_count += 1
            urls.add(product)
    print('%d products, after de-dup, %d left.' % (prodct_count, len(urls)))
    for url in urls:
        query = 'insert into source(url, enabled, created_at, updated_at) values("'
        query += url + '", true, now(), now());'
        print(query)

if __name__ == '__main__':
    main(parse_args())
