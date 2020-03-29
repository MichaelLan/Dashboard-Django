from django.urls import path
from .views import getDataId, getDataLocalidad, ProjectView, NewProjectView,NewProjectViewTest

core_patterns = ([
    path('', ProjectView.as_view(), name='home'),
    path('new', NewProjectView.as_view(), name='createProject'),
    path('new', NewProjectViewTest.as_view(), name='createProject2'),
    # path('', graphPageView.as_view(), name='home'),
    path('getdata/<int:id>/', getDataId, name='data'),
    path('getdataLocalidad/<slug:slug>/', getDataLocalidad, name='dataLocalidad'),
    path('newproject/', NewProjectView.as_view(), name='newproject')
], 'core')