from django.conf.urls import url
from django.contrib import admin
from .views import Time,HomePage,TimeAhead,current_datetime,HelloWorld
from  books import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage),
    url(r'^hello',HelloWorld),
    url(r'^Time/$',Time),
    url(r'^time_ahead/(\d{1,2})/$',TimeAhead),
    url(r'^curr/$',current_datetime),
    url(r'^search/$',views.search),
    url(r'^contact-func/$',views.contact_function),
    url(r'^contact-class/$',views.contact_class),
]																		 
     