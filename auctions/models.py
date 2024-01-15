from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class auctionlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    desc = models.TextField()  # CharField cannot be left without giving a max_length, Textfield can
    starting_bid = models.IntegerField()
    buy_now_price = models.IntegerField(default=0)
    image_url = models.CharField(max_length=228, default=None, blank=True, null=True)
    expire_date = models.DateTimeField(blank=False, null=True)
    categories = models.ManyToManyField('Category', through='AuctionCategory')
    active_bool = models.BooleanField(default=True)


class bids(models.Model):
    user = models.CharField(max_length=30)
    listingid = models.IntegerField()
    bid = models.IntegerField()


class comments(models.Model):
    user = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()


class watchlist(models.Model):
    watch_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64)


class winner(models.Model):
    bid_win_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64, default=None)


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class AuctionCategory(models.Model):
    auction = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
