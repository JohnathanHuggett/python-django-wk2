# Generated by Django 2.0.6 on 2018-06-25 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20180625_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='wed_address',
            new_name='web_address',
        ),
    ]
