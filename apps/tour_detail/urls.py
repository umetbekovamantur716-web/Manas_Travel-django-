from django.urls import path
from . import views

urlpatterns = [
    path('<int:tour_id>/', views.tour_detail_view, name='tour_detail'),
]

