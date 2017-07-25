""" Config """
# coding:utf-8

DB = {'host':'localhost',
      'user':'root',
      'passwd':'',
      'database':'bdsf',
      'charset':'utf8'}

QUEUE = {'host':'localhost',
         'port':'6379',
         'prefix':'bdsf'}

# TS = Task Status
TS_NEW = 'new'
TS_INPROGRESS = 'inprogress'
TS_FINISHED = 'finished'

# JS = Job Status
JS_NEW = 'new'
JS_FAILED = 'failed'
JS_FINISHED = 'finished'
