# Generated by Django 4.0.4 on 2022-05-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_personal_details',
            name='contact_num',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='employee_personal_details',
            name='emp_age',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='employee_personal_details',
            name='emp_salary',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='employee_personal_details',
            name='employee_id',
            field=models.IntegerField(default=False),
        ),
    ]
