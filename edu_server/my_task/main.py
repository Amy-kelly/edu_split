from celery import Celery
import os
import django

app = Celery("edu")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','edu_server.settings.develop')
django.setup()
#通过创建得实例对象加载配置
app.config_from_object("my_task.config")
app.autodiscover_tasks(['my_task.sms','my_task.change_order'])