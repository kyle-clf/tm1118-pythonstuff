from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('data_event', views.data_events),
    path('log', views.log),
    path('show/A07', views.showA07),
    path('test', views.test),
    path('dashboard', views.dashboard),
    path('dashboard-test', views.data_dashboard),
    path('data_dA01', views.data_dashboardA01),
    path('data_dA02', views.data_dashboardA02),
    path('data_dA03', views.data_dashboardA03),

]