""" Config for product spider """
# coding:utf-8

DB = {'host':'localhost',
      'user':'root',
      'passwd':'',
      'database':'fs_product',
      'charset':'utf8'}
      
QUEUE = {'host':'localhost',
         'port':'6379',
         'prefix':'fs_product'}

TS_NEW = 'new'
TS_INPROGRESS = 'inprogress'
TS_FINISHED = 'finished'

JS_NEW = 'new'
JS_FAILED = 'failed'
JS_FINISHED = 'finished'
