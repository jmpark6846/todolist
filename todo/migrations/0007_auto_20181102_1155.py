# Generated by Django 2.1.2 on 2018-11-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20181101_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.DateField(blank=True, null=True, verbose_name='마감기한'),
        ),
    ]
