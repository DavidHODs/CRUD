# Generated by Django 3.2 on 2021-05-03 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210503_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='image',
        ),
    ]
