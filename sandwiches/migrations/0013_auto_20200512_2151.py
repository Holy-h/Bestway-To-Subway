# Generated by Django 3.0.6 on 2020-05-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0012_auto_20200512_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='images/menus', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='cheese',
            field=models.ManyToManyField(to='sandwiches.Cheese', verbose_name='치즈'),
        ),
    ]
