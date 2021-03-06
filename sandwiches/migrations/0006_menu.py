# Generated by Django 3.0.6 on 2020-05-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0005_auto_20200511_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('en_name', models.CharField(default='', max_length=100, unique=True)),
                ('calorie', models.IntegerField(verbose_name='칼로리')),
                ('bio', models.TextField(blank=True, default='', verbose_name='설명')),
                ('limited', models.BooleanField(default=False, verbose_name='한정판매')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
