# Generated by Django 3.0.6 on 2020-05-12 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sandwiches', '0011_sandwich_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='bread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sandwiches', to='sandwiches.Bread', verbose_name='빵'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sandwiches', to='sandwiches.Menu', verbose_name='메뉴'),
        ),
        migrations.AlterField(
            model_name='sandwich',
            name='sauce',
            field=models.ManyToManyField(to='sandwiches.Sauce', verbose_name='소스'),
        ),
    ]
