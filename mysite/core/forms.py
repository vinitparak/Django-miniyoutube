from django import forms

from .models import Vibg


class VibgForm(forms.ModelForm):
    class Meta:
        model = Vibg
        fields = ('title','description','category','video', 'thumbnail')
