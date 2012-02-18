# encoding: utf-8
from django import forms

from plugins.models import Plugin, PluginDownload


class PluginForm(forms.ModelForm):

    class Meta:
        model = Plugin
        exclude = ['user']

class PluginUploadForm(forms.ModelForm):

    class Meta:
        model = PluginDownload
        exclude = ['plugin', 'upload_date']
