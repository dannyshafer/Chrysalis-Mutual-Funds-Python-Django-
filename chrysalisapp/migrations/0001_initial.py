# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('close', models.CharField(max_length=50, null=True)),
                ('high', models.CharField(max_length=50, null=True)),
                ('low', models.CharField(max_length=50, null=True)),
                ('price_open', models.CharField(max_length=50, null=True)),
                ('volume', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=50, null=True)),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('change', models.CharField(max_length=50, null=True)),
                ('volume', models.CharField(max_length=50, null=True)),
                ('prev_close', models.CharField(max_length=50, null=True)),
                ('stock_open', models.CharField(max_length=50, null=True)),
                ('avg_daily_volume', models.CharField(max_length=50, null=True)),
                ('stock_exchange', models.CharField(max_length=50, null=True)),
                ('market_cap', models.CharField(max_length=50, null=True)),
                ('book_value', models.CharField(max_length=50, null=True)),
                ('ebitda', models.CharField(max_length=50, null=True)),
                ('dividend_share', models.CharField(max_length=50, null=True)),
                ('dividend_yield', models.CharField(max_length=50, null=True)),
                ('earnings_share', models.CharField(max_length=50, null=True)),
                ('days_high', models.CharField(max_length=50, null=True)),
                ('days_low', models.CharField(max_length=50, null=True)),
                ('year_high', models.CharField(max_length=50, null=True)),
                ('year_low', models.CharField(max_length=50, null=True)),
                ('fifty_day_moving_avg', models.CharField(max_length=50, null=True)),
                ('two_hundred_day_moving_avg', models.CharField(max_length=50, null=True)),
                ('price_earnings_ratio', models.CharField(max_length=50, null=True)),
                ('price_earnings_growth_ratio', models.CharField(max_length=50, null=True)),
                ('price_sales', models.CharField(max_length=50, null=True)),
                ('price_book', models.CharField(max_length=50, null=True)),
                ('short_ratio', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
