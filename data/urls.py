from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('data_event', views.data_events),
    path('log', views.log),
    path('show/A07', views.showA07),
    path('test', views.test),
    path('dashboard', views.dashboard),
    path('dashboard-data', views.data_dashboard),
    path('data_test', views.data_test),
    path('data_test2', views.data_test2),
    path('data_dA01', views.data_dashboardA01),


]