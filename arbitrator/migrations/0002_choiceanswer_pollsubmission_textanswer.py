# Generated by Django 2.2.6 on 2019-12-05 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arbitrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateTimeField(auto_now=True, verbose_name='date submitted')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrator.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('poll_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrator.PollSubmission')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrator.Question')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrator.Choice')),
                ('poll_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbitrator.PollSubmission')),
            ],
        ),
    ]