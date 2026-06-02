from django.urls import path
from . import views

urlpatterns = [
    path('add-review/', views.reviews_page, name='add_review'),
    path('reviews/', views.all_reviews_view, name='all_reviews'),
]