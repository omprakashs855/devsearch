from django.urls import path
from . import views

urlpatterns = [
    
    path('projects', views.projects, name="projects"),
    path('products/<str:pk>/', views.products, name="products"),
]