# Generated by Django 2.2.1 on 2019-05-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_auto_20190517_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='CWURRank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
