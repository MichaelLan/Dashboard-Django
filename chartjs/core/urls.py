from django.urls import path
from .views import get_data_id, get_data_localidad, \
                ProjectView, NewProjectView

core_patterns = ([
    path('', ProjectView.as_view(), name='home'),
    path('new', NewProjectView.as_view(), name='cp'),
    path('getdata/<int:id>/', get_data_id, name='data'),
    path('getdataLocalidad/<slug:slug>/', get_data_localidad, name='dataLocalidad'),
], 'core')