from django import forms

class RewildForm(forms.Form):
    email_address = forms.EmailField()
    location_of_the_trees = forms.CharField()
    number_of_trees = forms.IntegerField()

    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
