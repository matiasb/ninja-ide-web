# -*- coding: utf-8 *-*
from django.contrib import admin

from plugins.models import Plugin, PluginDownload
from plugins.models import Vote


class PluginDownloadInline(admin.TabularInline):
    model = PluginDownload

class PluginAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'short_description', 'description', 'url', 'tags']
    list_filter = ['user', 'tags']
    search_fields = ['user', 'name', 'short_description', 'description', 'url', 'tags']
    inlines = [PluginDownloadInline]
admin.site.register(Plugin, PluginAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'plugin', 'rate', 'date', 'voter_ip']
    list_filter = ['user', 'plugin', 'rate', 'date', 'voter_ip']
    search_fields = ['user', 'plugin', 'rate', 'date', 'voter_ip']


admin.site.register(Vote, VoteAdmin)
