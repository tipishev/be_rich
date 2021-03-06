# Generated by Django 2.2.6 on 2020-01-18 12:49

import backend.transactions.enums
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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, backend.transactions.enums.AccountStatuses(0)), (1, backend.transactions.enums.AccountStatuses(1)), (2, backend.transactions.enums.AccountStatuses(2))], default=backend.transactions.enums.AccountStatuses(0))),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, backend.transactions.enums.AccountStatuses(0)), (1, backend.transactions.enums.AccountStatuses(1)), (2, backend.transactions.enums.AccountStatuses(2))], default=backend.transactions.enums.AccountStatuses(0))),
                ('currency', models.PositiveSmallIntegerField(choices=[(0, backend.transactions.enums.Currencies(0)), (1, backend.transactions.enums.Currencies(1)), (2, backend.transactions.enums.Currencies(2))], default=backend.transactions.enums.Currencies(0))),
                ('money', models.FloatField(default=0.0)),
                ('wallet_id', models.CharField(blank=True, max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Account')),
            ],
            options={
                'unique_together': {('account', 'currency')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('message', models.CharField(max_length=255)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, backend.transactions.enums.TransactionStatuses(0)), (1, backend.transactions.enums.TransactionStatuses(1)), (2, backend.transactions.enums.TransactionStatuses(2))], default=backend.transactions.enums.TransactionStatuses(1))),
                ('fee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.Transaction')),
                ('from_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_from', to='transactions.Wallet')),
                ('to_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_to', to='transactions.Wallet')),
            ],
        ),
    ]
