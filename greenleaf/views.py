from django.shortcuts import render

def catch_all(request, slug):
    return render(request, "{0}.html".format(slug))

def home(request):
    return render(request, "index.html")


def posts(request, slug):
    return render(request, "posts/{0}.html".format(slug))
