from django.contrib import admin
from .models import *


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    search_fields = ( 'title', 'user' )
    ordering = ( '-created_on', )
    list_display = ( 'title', 'user', 'slug', 'created_on', )
    list_filter = (  'title', 'user', 'slug', 'created_on', )
    fieldsets = (
        (None, { 'fields': ('user',)}),
        (None, { 'fields': ('title', 'slug', 'excerpt', 'category', )}),
        ('Website content', {'fields': ('body',)}),
        ('Status', {'fields': ('status',)}),
    )
