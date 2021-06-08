from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('', views.index),
    # path('maths/', include("maths.urls")),
]
