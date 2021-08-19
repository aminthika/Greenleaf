from django import forms

class RewildForm(forms.Form):
    trees = forms.IntegerField()
    location = forms.CharField()
    email= forms.EmailField()
    
    photo = forms.FileField(label="Upload a photo of one or more of your plants to confirm their existence\n", widget=forms.ClearableFileInput(attrs={'multiple': True}))
