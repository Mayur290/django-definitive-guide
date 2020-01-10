from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime

## simple hello world
def Homepage(request):
    return HttpResponse('<h1>Hello world</h1>')

## simple httpResponse of current time
def Time(request):
    now=datetime.datetime.now()
    html="<h1>current time is: %s.</h1>" % now
    return HttpResponse(html)

## simple httpResponse of future time
def TimeAhead(request,offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404("timeAhead should be in digits")
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)    
	html= "<p>time ahead %s hours is: %s .</p>" % (offset,dt)
	return  HttpResponse(html) 

## dynamic template of current time
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render(request,'current_datetime.html',locals())