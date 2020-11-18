from django.urls import path
from . import views

urlpatterns = [
    path('', views.math_index),
    path('binomial/', views.binomial_distribution),
    path('poisson/', views.poisson_distribution),
    path('normal/', views.normal_distribution),
    path('binomial/calculate', views.calculate_binomial_distribution),
    path('poisson/calculate', views.calculate_poisson_distribution),
    path('normal/calculate', views.calculate_normal_distribution),
]
