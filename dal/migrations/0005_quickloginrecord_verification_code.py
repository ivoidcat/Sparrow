# Generated by Django 2.0 on 2018-05-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dal', '0004_quickloginrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickloginrecord',
            name='verification_code',
            field=models.CharField(default='', max_length=512, null=True),
        ),
    ]
