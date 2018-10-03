from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/opinia', views.index, name='opinia_new'),
]
