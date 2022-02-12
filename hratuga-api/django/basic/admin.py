from django.contrib import admin

from .models import *


@admin.register(Group)
class Group(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)
    list_filter = ('question',)
    search_fields = ('question',)


@admin.register(PackingListTag)
class PackingListTag(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(PackingList)
class PackingList(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(PackingListItem)
class PackingListItem(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(NewsBox)
class NewsBox(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
