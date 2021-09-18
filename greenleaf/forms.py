from django import forms

class RewildForm(forms.Form):
<<<<<<< HEAD
    name = forms.CharField(label="your first and last name")
=======
>>>>>>> 75b29a0e14cae0007467984f1c224b215ff368a8
    trees = forms.IntegerField(label="number of trees planted")
    location = forms.CharField(label="location of the trees")
    email= forms.EmailField(label="email address")
    
    photo = forms.FileField(label="Upload a photo of one or more of your plants to confirm their existence\n", widget=forms.ClearableFileInput(attrs={'multiple': True}))
