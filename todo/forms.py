# coding:utf-8
from django import forms

from .models import TodoEnvet

class TodoEnvetForm(forms.ModelForm):

    class Meta:
        model = TodoEnvet
        fields = ('event_name',)