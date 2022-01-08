from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    author_name = forms.CharField(max_length=30, required=True, label='Имя')
    author_mail = forms.CharField(required=True, label="Email", widget=widgets.EmailInput())
    text_notes = forms.CharField(max_length=2000, required=True, label='Текст',
                                 widget=widgets.Textarea(attrs={"rows": 5, "cols": 30}))
