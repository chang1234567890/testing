

from django.db import models

# Create your models here.
from django.utils import timezone


class Test(models.Model):
    client = models.CharField(max_length=20, verbose_name='客户端')
    stock = models.IntegerField(max_length=20, verbose_name='分数')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)