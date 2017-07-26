""" Worker """
# coding:utf-8

import argparse
import datetime as dt
import importlib
import multiprocessing
import threading
import time
import traceback
import ds_database as dd
import ds_queue as dq

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--config',
                        default='ds_config') # # Assign config file, don't use '.py' suffix.
    parser.add_argument('-s',
                        '--spider',
                        help='',
                        default='spider_sample') # Assign spider file, don't use '.py' suffix.
    parser.add_argument('-t',
                        '--thread_count',
                        help='',
                        default=0,
                        type=int)
    return parser.parse_args()

def woker(spider, database, config):
    while True:
        try:
            for task in dd.Task.select().where(dd.Task.status == config.TS_INPROGRESS):
                print('Process task %d.' % task.id)
                queue = dq.Queue(task.id, config.QUEUE)
                while not queue.empty():
                    job = queue.get(False)
                    if job:
                        parse_result = spider.parse(eval(job), config)
                        content = parse_result['content']
                        if content:
                            result = dd.Result.select().where(dd.Result.source_id == parse_result['source_id'])
                            if result: # Update result
                                result = result.get()
                                result.updated_at = dt.datetime.now()
                            else: # Insert new result
                                result = dd.Result()
                                result.source_id = parse_result['source_id']
                            result.content = content
                            result.save()
                        # Update job status
                        job = dd.Job.select().where(dd.Job.id == parse_result['id']).get()
                        job.status = parse_result['status']
                        job.message = parse_result['message']
                        job.updated_at = dt.datetime.now()
                        job.save()
                time.sleep(15) # Sleep 15 seconds if there is no job in the queue for the task.
        except Exception as e:
            print('%s\n%s' % (e, traceback.format_exc()))

def main(args):
    thread_count = args.thread_count
    config = importlib.import_module(args.config)
    spider = importlib.import_module(args.spider) # Load spider implementation
    database = dd.init_database(config.DB)
    threads = []
    for i in range(multiprocessing.cpu_count() if thread_count <= 0 else thread_count):
        threads.append(threading.Thread(target=woker, args=(spider, database, config)))
    for t in threads:
        t.daemon = True # Or you can't terminate by Ctrl-C
        t.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        exit()
if __name__ == '__main__':
    main(parse_args())
