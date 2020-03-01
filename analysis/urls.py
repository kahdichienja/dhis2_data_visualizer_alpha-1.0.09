from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('map/', views.mapdata, name= 'mapdata'),
    path('api/endpoint/', views.queryApi, name = 'apidata'),
    path('megasearch/', views.customSearchView, name = 'customsearch'),
    # path('prediction/', views.prediction(), name = 'prediction'),
]


