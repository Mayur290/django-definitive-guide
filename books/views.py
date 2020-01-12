# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search_form(request):
    return render(request,"search_form.html")

def search(request):
    error = False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error = True
        elif len(q)>20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,"search_results.html",{'books':books,'query':q})
    return render(request,"search_form.html",{'error':error})