# Generated by Django 2.2.4 on 2019-08-26 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0009_conference_contact_email'),
        ('chair_mail', '0002_auto_20190824_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('assign_status_review', 'Assign status review to the paper'), ('assign_status_submit', 'Assign status submit to the paper')], max_length=64)),
                ('subject', models.CharField(blank=True, max_length=1024)),
                ('is_active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('user', 'Message to users'), ('submission', 'Message to submissions')], max_length=64)),
                ('body', models.TextField(blank=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='conferences.Conference')),
            ],
        ),
        migrations.AddConstraint(
            model_name='systemnotification',
            constraint=models.UniqueConstraint(fields=('conference', 'name'), name='unique_name'),
        ),
    ]
