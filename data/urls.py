from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('data_event', views.data_events),
    path('log', views.log),
    path('show/A07', views.showA07),
    path('test', views.test),
    path('dashboard', views.dashboard),

]