from django.urls import path
from gold.views import *
app_name='something'
urlpatterns=[
    path('rings/',rings,name='rings'),
]