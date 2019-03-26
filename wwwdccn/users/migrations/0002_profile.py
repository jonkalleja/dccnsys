# Generated by Django 2.1.7 on 2019-03-26 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name in English')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name in English')),
                ('first_name_rus', models.CharField(default='', max_length=100, verbose_name='First Name in Russian')),
                ('middle_name_rus', models.CharField(default='', max_length=100, verbose_name='Middle Name in Russian')),
                ('last_name_rus', models.CharField(default='', max_length=100, verbose_name='Last Name in Russian')),
                ('avatar', models.ImageField(blank=True, upload_to=users.models.get_avatar_full_path)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('affiliation', models.CharField(max_length=100, verbose_name='Name of your organization in English')),
                ('role', models.CharField(choices=[(None, 'Select your role'), ('Student', 'Student'), ('PhD Student', 'PhD Student'), ('Assistant', 'Assistant'), ('Researcher', 'Researcher'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor'), ('Head of Department', 'Head of Department'), ('Head of Faculty', 'Head of Faculty'), ('Head of Laboratory', 'Head of Laboratory'), ('Vice Rector', 'Vice Rector'), ('Rector', 'Rector'), ('Software Developer', 'Software Developer'), ('Engineer', 'Engineer'), ('Technician', 'Technician'), ('Economist', 'Economist'), ('Lawyer', 'Lawyer'), ('Instructor', 'Instructor'), ('Consultant', 'Consultant'), ('Manager', 'Manager'), ('Administrator', 'Administrator'), ('Analyst', 'Analyst'), ('Journalist', 'Journalist'), ('Writer', 'Writer'), ('Editor', 'Editor'), ('Librarian', 'Librarian'), ('Vice Director', 'Vice Director'), ('Chief Executive Officer', 'Chief Executive Officer'), ('Retired', 'Retired'), ('Other', 'Other')], max_length=30, null=True, verbose_name='Primary role in organization')),
                ('degree', models.CharField(choices=[(None, 'Select your degree'), ('Undergraduate', 'Undergraduate'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('PhD', 'PhD'), ('Candidate of Sciences', 'Candidate of Sciences'), ('Doctor of Sciences', 'Doctor of Sciences')], max_length=30, null=True, verbose_name='Degree')),
                ('ieee_member', models.BooleanField(verbose_name='I am an IEEE Member')),
                ('preferred_language', models.CharField(choices=[('ENG', 'English'), ('RUS', 'Russian')], default='ENG', max_length=3)),
                ('agree_to_receive_emails', models.BooleanField(default=False, verbose_name='I agree to receive emails from DCCN Registration System')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]