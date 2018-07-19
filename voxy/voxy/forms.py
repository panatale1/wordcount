"""Forms for Voxy Word Count app"""
from django import forms


class WordCountForm(forms.Form):
    # This form only needs one field
    text_block = forms.CharField(
        widget=forms.Textarea(),
        error_messages={'required': 'Please enter some text'}
    )
