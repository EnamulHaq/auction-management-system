# Generated by Django 5.0.1 on 2024-01-15 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auctionlist_buy_now_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='expire_date',
            field=models.DateTimeField(default=datetime.date(2024, 1, 15)),
        ),
    ]
