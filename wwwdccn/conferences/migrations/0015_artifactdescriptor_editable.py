# Generated by Django 2.2.4 on 2019-10-03 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0014_artifactdescriptor_mandatory'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifactdescriptor',
            name='editable',
            field=models.BooleanField(default=True),
        ),
    ]
