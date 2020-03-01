from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('map/', views.mapdata, name= 'mapdata'),
    path('api/endpoint/', views.queryApi, name = 'apidata'),
    path('megasearch/', views.customSearchView, name = 'customsearch'),
    path('mega/', views.customAjaxSearchView, name = 'mega'),
    path('mapdataIframe/', views.mapdataIframe, name = 'mapdataIframe'),
]


