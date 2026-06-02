from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('tours/', views.turs_home, name='turs_home'),
    path('search/', views.search_tours_view, name='search_tours')   
]