# Generated by Django 2.2.6 on 2019-11-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbitrator', '0002_auto_20191120_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='multiple_selection',
            field=models.BooleanField(default=False),
        ),
    ]