# Generated by Django 4.0.1 on 2022-07-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_img',
            field=models.ImageField(default='', upload_to='profile/images'),
        ),
    ]
