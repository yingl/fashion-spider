""" Check result to find out what's missing """
# coding:utf-8

import argparse
import sys
import urllib.parse
sys.path.append('../')
import product_config as pc
import ds_database as dd

def write_to_file(file, lines):
    with open(file, 'w+', encoding='utf-8') as f:
        for line in lines:
            if line:
                f.write(line + '\n')

def main():
    dd.init_database(pc.DB)
    sources = dd.Source.select()
    results = dd.Result.select()
    data = {}
    for source in sources:
        data[source.id] = {'url':source.url}
    for result in results:
        if result.source_id in data:
            data[result.source_id]['content'] = eval(result.content)
    rows = []
    for k, v in data.items():
        if 'content' in v:
            title = v['content']['title'].replace('\n', '%0A')
            images = v['content']['images'].replace(' ', '%20')
            images = images.replace('\n', '%0A')
            line = '{'
            line += "'url':'" + v['url'] + "',"
            line += "'brand':'" + v['content']['brand'] + "',"
            line += "'title':'" + title + "',"
            line += "'code':'" + v['content']['code'] + "',"
            line += "'price':" + str(v['content']['price']) + ","
            line += "'images':'" + images + "'"
            line += '}'
            rows.append(line)
    sorted(rows)
    print('Rows: %d' % len(rows))
    write_to_file('products.txt', rows)

if __name__ == '__main__':
    main()