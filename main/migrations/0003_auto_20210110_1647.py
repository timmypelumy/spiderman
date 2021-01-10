# Generated by Django 3.1.4 on 2021-01-10 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_withdrawalrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawalrequest',
            old_name='email',
            new_name='client',
        ),
        migrations.AddField(
            model_name='withdrawalrequest',
            name='date_filed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
