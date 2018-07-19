from django import forms


class WordCountForm(forms.Form):
    text_block = forms.CharField(
        widget=forms.Textarea(),
        error_messages={'required': 'Please enter some text'})
