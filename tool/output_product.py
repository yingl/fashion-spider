""" Check result to find out what's missing """
# coding:utf-8

import argparse
import sys
import urllib.parse
sys.path.append('../')
import product_config as pc
import ds_database as dd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b',
                        '--brand',
                        help='Specify the brand you want to fetch',
                        default='')
    parser.add_argument('-f',
                        '--filename',
                        help='Specify the filename you want to save data',
                        default='')
    return parser.parse_args()

def write_to_file(file, lines):
    with open(file, 'w+', encoding='utf-8') as f:
        for line in lines:
            if line:
                f.write(line + '\n')

def main():
    args = parse_args()
    dd.init_database(pc.DB)
    results = dd.Result.select().where(dd.Result.content.contains(args.brand))
    rows = []
    for result in results:
        rows.append(result.content)
    sorted(rows)
    print('Rows: %d' % len(rows))
    write_to_file(args.filename, rows)

if __name__ == '__main__':
    main()