# Generated by Django 2.2.14 on 2020-07-06 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=20, verbose_name='客户端')),
                ('stock', models.IntegerField(max_length=20, verbose_name='分数')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
            ],
        ),
    ]
