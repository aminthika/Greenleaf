from django import forms

class RewildForm(forms.Form):
    email = forms.EmailField()
    location = forms.CharField()
    trees = forms.IntegerField()

    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))