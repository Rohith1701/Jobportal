# Generated by Django 3.2 on 2023-06-12 07:28

import JobPortal.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortal', '0002_alter_userwithrole_companyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='resume',
            field=models.FileField(upload_to='static/resume/', validators=[JobPortal.validators.validate_file_extension]),
        ),
    ]
