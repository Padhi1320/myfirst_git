from django.urls import path
from sum2.views import *
app_name='anything2'


urlpatterns=[
    path('Suresh/',Suresh, name='suresh'),
    path('Furesh/', Furesh, name='Furesh'),

]