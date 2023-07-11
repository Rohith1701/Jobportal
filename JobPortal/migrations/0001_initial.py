# Generated by Django 3.2 on 2023-06-01 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWithRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(default='first name', max_length=200)),
                ('last_name', models.CharField(default='last name', max_length=200)),
                ('companyname', models.CharField(max_length=200)),
                ('dob', models.DateField(default='dob')),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='select gender', max_length=200)),
                ('mobile', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password1', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('hr', 'hr'), ('candidate', 'candidate')], max_length=200)),
                ('create_by', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('Location', models.CharField(max_length=2000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='static/resume/')),
                ('candidate_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.userwithrole', verbose_name='Candidate Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.company')),
            ],
        ),
    ]
