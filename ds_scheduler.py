""" Scheduler """
# coding:utf-8

import argparse
import datetime as datetime
import importlib
import ds_database as dd
import ds_queue as dq

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--config',
                        default='ds_config') # Assign config file, don't use '.py' suffix.
    parser.add_argument('-a',
                        '--action',
                        default='create') # Actions: create/view/retry
    parser.add_argument('-t',
                        '--task_id',
                        default=0,
                        type=int)
    return parser.parse_args()

def create_task(config):
    task = dd.Task(status=config.TS_NEW)
    task.save()
    queue = dq.Queue(task.id, config.QUEUE) # Create distributed queue for jobs.
    # select * from source where enabled = True
    sources = dd.Source.select().where(dd.Source.enabled)
    # Create jobs and send to queue
    for source in sources:
        job = dd.Job(task_id=task.id, source_id=source.id, status=config.JS_NEW)
        job.save()
        queue.put({'id':job.id, 'source_id':source.id, 'url':source.url})
    task.status = config.TS_INPROGRESS
    task.jobs = len(sources)
    task.save()
    print('Task %d is scheduled with %d jobs.' % (task.id, task.jobs))
    
def view_task(task_id, config):
    r = dd.Task.select().where(dd.Task.id == task_id)
    if r:
        task = r.get()
        if task.status == config.TS_INPROGRESS:
            jobs = dd.Job.select().where(dd.Job.task_id == task_id)
            unfinished = 0
            finished = 0
            failed = 0
            for job in jobs:
                if job.status == config.JS_FINISHED:
                    finished += 1
                elif job.status == config.JS_FAILED:
                    failed += 1
                elif job.status == config.JS_NEW:
                    unfinished += 1
            task.unfinished = unfinished
            task.finished = finished
            task.failed = failed
            if (task.jobs == (finished + failed)) and (unfinished == 0):
                task.status = config.TS_FINISHED
            task.save()
            print('%d jobs for task %d: %d finished, %d failed.' % (task.jobs, task.id, task.finished, task.failed))
        elif task.status == config.TS_FINISHED:
            print('%d jobs for task %d: %d finished, %d failed.' % (task.jobs, task.id, task.finished, task.failed))
        elif task.status == config.TS_NEW:
            print('Task %d not scheduled yet.' % task_id)
    else:
        raise Exception('Task %d not found.' % task_id)

def retry(task_id, config):
    r = dd.Task.select().where(dd.Task.id == task_id)
    if r:
        task = r.get()
        queue = dq.Queue(task.id, config.QUEUE) # 找到task对应的队列
        jobs = dd.Job.select().where((dd.Job.task_id == task_id) & (dd.Job.status != config.JS_FINISHED))
        for job in jobs:
            source = dd.Source.select().where(dd.Source.id == job.source_id).get()
            queue.put({'id':job.id, 'source_id':source.id, 'url':source.url})
            job.status = config.JS_NEW
            job.save()
        task.status = config.TS_INPROGRESS
        task.failed = 0
        task.unfinished = len(jobs)
        task.save()
        print('Retry %d jobs of task %d' % (len(jobs), task_id))
    else:
        raise Exception('Task %d not found.' % task_id)

def main():
    args = parse_args()
    # Use dynamic loading for config file, then we can use different config file for different task.
    config = importlib.import_module(args.config)
    dd.init_database(config.DB)
    if args.action == 'create':
        create_task(config)
    elif args.action == 'view':
        view_task(args.task_id, config)
    elif args.action == 'retry':
        retry(args.task_id, config)
    else:
        raise Exception('Unknown action: %s' % args.action)

if __name__ == '__main__':
    main()
