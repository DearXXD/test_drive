# coding:utf-8
from django.db import models
# Create your models here.


class TodoEvent(models.Model):
    event_name = models.CharField(max_length=1024, verbose_name='待办事项名称')
