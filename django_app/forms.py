from .models import post
from django import forms


class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'
