from django import forms

class RewildForm(forms.Form):
    trees = forms.IntegerField(label="number of trees planted")
    location = forms.CharField(label="location of the trees")
    email= forms.EmailField(label="email address")
    
    photo = forms.FileField(label="Upload a photo of one or more of your plants to confirm their existence\n", widget=forms.ClearableFileInput(attrs={'multiple': True}))
