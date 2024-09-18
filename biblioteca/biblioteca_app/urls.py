from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # HTML
    path('shelf/<int:shelf_id>/', views.shelf_detail, name='shelf_detail'), # HTML
    path('filter-books/', views.filter_books, name='filter_books'), # JS
]
