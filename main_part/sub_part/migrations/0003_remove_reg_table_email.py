# Generated by Django 4.0.1 on 2022-01-26 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_reg_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_table',
            name='email',
        ),
    ]
