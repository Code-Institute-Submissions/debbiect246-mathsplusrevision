from django.shortcuts import render, redirect, reverse

# Create your views here.


def blog(request):
    """A View that renders the blog contents page"""
    return render(request, "blog.html")
