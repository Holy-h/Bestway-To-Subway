# Generated by Django 3.0.6 on 2020-05-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0010_sandwich_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='orders',
            field=models.IntegerField(blank=True, default=0, verbose_name='주문수'),
        ),
    ]
