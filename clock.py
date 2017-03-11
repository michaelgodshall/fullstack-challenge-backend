from apscheduler.scheduler import Scheduler
from rq import Queue
from worker import conn
from django.core.management import call_command

q = Queue(connection=conn)

sched = Scheduler()


# @sched.cron_schedule(second=30)
# @sched.interval_schedule(minutes=1)
# def update_statuses():
#     q.enqueue(call_command('update_messages'))

sched.start()

while True:
    pass