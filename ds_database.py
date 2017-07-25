""" MySQL database """
# coding:utf-8

import inspect
import datetime as dt
import sys
import traceback
from peewee import BooleanField # peewee相关模块
from peewee import CharField
from peewee import DateTimeField
from peewee import IntegerField
from peewee import Model
from peewee import MySQLDatabase
from peewee import TextField

class Task(Model):
    status = CharField()
    jobs = IntegerField(default=0)
    finished = IntegerField(default=0)
    unfinished = IntegerField(default=0)
    failed = IntegerField(default=0)
    created_at = DateTimeField(default=dt.datetime.now)
    updated_at = DateTimeField(default=dt.datetime.now)
    class Meta:
        database = None

class Job(Model):
    task_id = IntegerField()
    source_id = IntegerField()
    status = CharField()
    message = TextField(default='')
    created_at = DateTimeField(default=dt.datetime.now)
    updated_at = DateTimeField(default=dt.datetime.now)
    class Meta:
        database = None

class Source(Model):
    url = TextField()
    enabled = BooleanField(default=True)
    created_at = DateTimeField(default=dt.datetime.now)
    updated_at = DateTimeField(default=dt.datetime.now)
    class Meta:
        database = None

class Result(Model):
    content = TextField()
    source_id = IntegerField()
    created_at = DateTimeField(default=dt.datetime.now)
    updated_at = DateTimeField(default=dt.datetime.now)
    class Meta:
        database = None

def init_database(config):
    db = MySQLDatabase(host=config['host'],
                       user=config['user'],
                       passwd=config['passwd'],
                       database=config['database'],
                       charset=config['charset'])
    for var in dir(sys.modules[__name__]): # Load tables dynamically
        if var != 'Model':
            obj = eval(var)
            if inspect.isclass(obj) and issubclass(obj, Model):
                # About meta programming, refer https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
                obj._meta.database = db
    return db

if __name__ == '__main__':
    DATABASE = None
    try:
        import ds_config as dc # You can modify the code to load different config dynamically
        DATABASE = init_database(dc.DB)
        TABLES = []
        for var in dir(sys.modules[__name__]):
            if var != 'Model':
                obj = eval(var)
                if inspect.isclass(obj) and issubclass(obj, Model):
                    TABLES.append(obj)
        DATABASE.connect()
        DATABASE.create_tables(TABLES, safe=True)
    except Exception as e:
        print('%s\n%s' % (e, traceback.print_exc()))
    finally:
        if DATABASE:
            DATABASE.close()
