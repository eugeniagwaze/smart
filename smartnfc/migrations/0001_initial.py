# Generated by Django 5.0.4 on 2024-04-09 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(blank=True, max_length=50, unique=True)),
                ('documents', models.FileField(blank=True, upload_to='documents/')),
                ('approval_status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('trans_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('currency', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(blank=True, max_length=8, unique=True)),
                ('currency', models.CharField(blank=True, max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('dual_account', models.CharField(blank=True, max_length=50, unique=True)),
                ('amount_zig', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('amount_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('cell_number', models.CharField(blank=True, max_length=15)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_wallets', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('trans_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('amount_deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('currency', models.CharField(blank=True, max_length=50)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to='smartnfc.wallet')),
            ],
        ),
    ]