from django.urls import path
from app1 import views
from django.conf.urls import url

app_name='app1'

urlpatterns = [
    path('',views.todoListView.as_view(),name='list'),
    path('create/',views.CreatetodoView.as_view(),name='create'),
    url(r'^(?P<pk>[-\w]+)/$',views.todoDetailView.as_view(),name='detail'),
    url(r'^update/(?P<pk>[-\w]+)/$',views.UpdatetodoView.as_view(),name='update'),
    url(r'^delete/(?P<pk>[-\w]+)/$',views.DeletetodoView.as_view(),name='delete'),
]
