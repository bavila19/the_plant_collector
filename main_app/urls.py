from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('about/', views.About.as_view(), name="about"), # <- new route
    path('plants/', views.PlantList.as_view(), name="plant_list" )
]