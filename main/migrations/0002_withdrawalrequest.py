# Generated by Django 3.1.4 on 2021-01-10 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=48)),
                ('amount', models.PositiveIntegerField()),
                ('mode', models.CharField(choices=[('bank', 'bank'), ('wallet', 'wallet')], max_length=25)),
                ('wallet_type', models.CharField(blank=True, choices=[('bitcoin', 'bitcoin'), ('eth', 'eth')], max_length=25)),
                ('wallet_addr', models.CharField(blank=True, max_length=72)),
                ('bank_name', models.CharField(blank=True, max_length=128)),
                ('bank_acct_no', models.CharField(blank=True, max_length=25)),
                ('bank_swift', models.CharField(blank=True, max_length=16)),
                ('desc', models.TextField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]