from django.urls import path
from .views import graphPageView, getDataId, getDataLocalidad, NewProjectView

core_patterns = ([
    path('', graphPageView.as_view(), name='home'),
    path('getdata/<int:id>/', getDataId, name='data'),
    path('getdataLocalidad/<slug:slug>/', getDataLocalidad, name='dataLocalidad'),
    path('newproject/', NewProjectView.as_view(), name='newproject')
], 'core')