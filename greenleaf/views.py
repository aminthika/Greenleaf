from django.shortcuts import render, reverse, redirect
from django.db.models import Sum
from greenleaf import forms
from greenleaf.models import RewildPhoto, Rewild

def catch_all(request, slug):
    return render(request, "{0}.html".format(slug))

def home(request):
    return render(request, "index.html")


def posts(request, slug):
    return render(request, "posts/{0}.html".format(slug))

def rewild_display(request):
    objects = Rewild.objects.all()
    total_trees = Rewild.objects.aggregate(Sum('trees'))['trees__sum']
    goal = 100
    percentage = total_trees / goal * 100
    return render(request, "rewild.html", {'rewilds': objects, 'percentage' : percentage, 'goal' : goal, 'total' : total_trees} )

def rewild(request):
    if request.method == 'POST':
        form = forms.RewildForm(request.POST, request.FILES)
        if form.is_valid():
            rewild = Rewild.objects.create( name=form.cleaned_data['name'],
            email=form.cleaned_data['email'], location=form.cleaned_data['location'], 
            trees=form.cleaned_data['trees']),

            for file in request.FILES.getlist('photo'):
                RewildPhoto.objects.create(rewild=rewild, image=file)

            return redirect(reverse("thank"))   
    else:
        form = forms.RewildForm()
    objects = Rewild.objects.all()
    total_trees = Rewild.objects.aggregate(Sum('trees'))['trees__sum']
    goal = 100
    percentage = total_trees / goal * 100
    return render(request, "rewild.html", {'form': form, 'rewilds': objects, 'percentage' : percentage, 'goal' : goal, 'total' : total_trees} )


    