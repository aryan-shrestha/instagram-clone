# Generated by Django 4.1.3 on 2022-12-03 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_story_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='viwed_by',
            new_name='views',
        ),
    ]