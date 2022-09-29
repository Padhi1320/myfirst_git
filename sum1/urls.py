from django.urls import path
from sum1.views import *
app_name='anything'

urlpatterns=[
    path('Ajaya/',Ajaya ,name='Ajaya'),
    path('Con/',Con, name='con'),
]