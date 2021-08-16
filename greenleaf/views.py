from django.shortcuts import render, reverse, redirect

from greenleaf import forms
from greenleaf.models import RewildPhoto, Rewild

def catch_all(request, slug):
    return render(request, "{0}.html".format(slug))

def home(request):
    return render(request, "index.html")


def posts(request, slug):
    return render(request, "posts/{0}.html".format(slug))


def rewild(request):
    if request.method == 'POST':
        form = forms.RewildForm(request.POST, request.FILES)
        if form.is_valid():
            rewild = Rewild.objects.create(email=form.cleaned_data['email'],
                location=form.cleaned_data['location'], trees=form.cleaned_data['trees'])

            for file in request.FILES.getlist('photo'):
                RewildPhoto.objects.create(rewild=rewild, image=file)

            return redirect(reverse("thank"))   
    else:
        form = forms.RewildForm()

    return render(request, "rewild.html", {'form': form})


    