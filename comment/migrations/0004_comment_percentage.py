# Generated by Django 3.0.2 on 2021-01-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='percentage',
            field=models.FloatField(default=0.0),
        ),
    ]
