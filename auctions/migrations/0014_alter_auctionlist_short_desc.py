# Generated by Django 5.0.1 on 2024-01-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auctionlist_bid_watch_list_alter_auctionlist_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='short_desc',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
