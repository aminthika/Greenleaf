from django import forms

class RewildForm(forms.Form):
    number_of_trees = forms.IntegerField()
    location_of_the_trees = forms.CharField()
    email_address = forms.EmailField()
    
    photo = forms.FileField(label="Upload a photo of one or more of your plants to confirm their existence\n", widget=forms.ClearableFileInput(attrs={'multiple': True}))
