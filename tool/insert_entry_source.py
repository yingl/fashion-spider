""" Build the queries to insert entry urls """
# coding:utf-8
import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                query = 'insert into source(url, enabled, created_at, updated_at) values('
                query += '"' + line + '", '
                query += 'True, now(), now());'
                print(query)