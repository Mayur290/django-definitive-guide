from django.conf.urls import url
from django.contrib import admin
from .views import Time,Homepage,TimeAhead,current_datetime

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Homepage),
    url(r'^Time/$',Time),
    url(r'^time_ahead/(\d{1,2})/$',TimeAhead),
    url(r'^curr/$',current_datetime),
]																		 
    