from django.contrib import admin
from .models import *


# Register your models here.
class AuctionCategoryAdmin(admin.TabularInline):
    model = AuctionCategory
    extra = 1


class auction(admin.ModelAdmin):
    inlines = [
        AuctionCategoryAdmin,
    ]
    list_display = ("id", "user", "active_bool", "title", "desc", "starting_bid", "buy_now_price", "image_url")


class watchl(admin.ModelAdmin):
    list_display = ("id", "watch_list", "user")


class bds(admin.ModelAdmin):
    list_display = ("id", "user", "listingid", "bid")


class comme(admin.ModelAdmin):
    list_display = ("id", "user", "comment", "listingid")


class win(admin.ModelAdmin):
    list_display = ("id", "user", "bid_win_list")


class user(admin.ModelAdmin):
    list_display = ("id", "username", "email")


class category(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(auctionlist, auction)
admin.site.register(bids, bds)
admin.site.register(comments, comme)
admin.site.register(watchlist, watchl)
admin.site.register(winner, win)
admin.site.register(User, user)
admin.site.register(Category, category)
