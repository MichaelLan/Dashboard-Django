from django.urls import path
from .views import graphPageView, getDataId

core_patterns = ([
    path('', graphPageView.as_view(), name='home'),
    path('getdata/<int:id>/', getDataId, name='data')
], 'core')