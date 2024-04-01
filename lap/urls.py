from django.urls import path
from lap.views import *
app_name='anything'
urlpatterns=[
    path('dell/',dell,name='dell')
    
]