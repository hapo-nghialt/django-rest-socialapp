# Generated by Django 2.0.5 on 2018-09-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
