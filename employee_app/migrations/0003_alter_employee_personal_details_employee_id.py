# Generated by Django 4.0.4 on 2022-05-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'employee_app',
            '0002_alter_employee_personal_details_contact_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_personal_details',
            name='employee_id',
            field=models.IntegerField(blank=True, default=0, max_length=5),
        ),
    ]
