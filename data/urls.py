from django.urls import path

from . import views

urlpatterns = [
    
    # views
    path('', views.dashboard),
    path('dashboard', views.dashboard),
 
    path('query', views.queryForm),
    path('query/result', views.queryResult),
    path('log', views.log),
    path('logd', views.logd),
    path('excel' ,views.excel),
  
    # data
    path('data_event', views.data_events),
    path('dashboard-data', views.data_dashboard),
    # test
    path('graph/overview', views.graph_overview),
    path('location', views.location),


    path('index', views.index),
    path('show/A07', views.showA07),
    path('test', views.test),
   
    
    path('data_test', views.data_test),
    path('data_test2', views.data_test2),
   
    path('data_dA01', views.data_dashboardA01),


]