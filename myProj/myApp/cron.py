from django_cron import CronJobBase, Schedule
from . import models

def my_scheduled_job():
  req = models.Crontab(titre='Salut')
  req.save()

# from django_cron import CronJobBase, Schedule

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 120 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'mypp.my_cron_job'    # a unique code

#     def do(self):
#       var =print('======= ok')
#       return var
#     print('--------- zo')