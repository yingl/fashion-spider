""" Config for entry spider """
# coding:utf-8

DB = {'host':'localhost',
      'user':'root',
      'passwd':'',
      'database':'fs_entry',
      'charset':'utf8'}
      
REDIS = {'host':'localhost',
         'port':'6379',
         'prefix':'dks'}

TS_NEW = 'new'
TS_INPROGRESS = 'inprogress'
TS_FINISHED = 'finished'

JS_NEW = 'new'
JS_FAILED = 'failed'
JS_FINISHED = 'finished'
