# Generated by Django 4.0.1 on 2022-01-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_rename_first_name_reg_table_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('group', models.CharField(max_length=20)),
            ],
        ),
    ]
