from .models import post, post_post, post123
from django import forms


class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'


class post_py(forms.ModelForm):
    class Meta:
        model = post_post
        fields = ['name', 'username', 'img']


class post123_form(forms.ModelForm):
    class Meta:
        model = post123
        fields = ['name', 'username', 'img1', 'img']
