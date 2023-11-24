from django.urls import path, include
from .sampleView import SampleView


app_name = 'sample'

urlpatterns = [
    path('view/', SampleView.as_view(), name='sample')
]