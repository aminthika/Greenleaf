from django import forms

class RewildForm(forms.Form):
    email_address = forms.EmailField()
    number_of_trees = forms.IntegerField()
    location_of_the_trees = forms.CharField()
    
    photo = forms.FileField(label="Upload a photo of one or more of your plants to confirm their existence\n", widget=forms.ClearableFileInput(attrs={'multiple': True}))
