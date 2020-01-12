# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
from django.core.mail import  send_mail
from books.forms import ContactForm


def search(request):
    errors = []
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter a search item.')
        elif len(q)>20:
            errors.append('Please enter atmost 20 items. ')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request,"search_results.html",{'books':books,'query':q})
    return render(request,"search_form.html",{'errors':errors})


def contact_function(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('e-mail','noreply@example.com'),
                ['mayurbansal98@gmail.com'],
            )
            return HttpResponseRedirect('/contacts/thanks/')
    return render(request,'contact_form0.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'e-mail': request.POST.get('e-mail', ''),
    })
    
    
def contact_class(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(
			cd['subject'],
			cd['message'],
			cd.get('e-mail', 'noreply@example.com'),
			['siteowner@example.com'],
			)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial = {'subject':'I love your site!'})
    return render(request,'contact_form.html', {'form': form})