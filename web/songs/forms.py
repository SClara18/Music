from django import forms
from django.db.models import fields
from .models import Songs

class SongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['tittle','artist','year','genre']
        