import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphics_in_the_admin_panel_project.settings')

app = Celery('graphics_in_the_admin_panel_application')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()


