# Generated by Django 4.0.1 on 2022-08-01 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_remove_employee_profile_img_remove_employee_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
