from django.urls import path
from . import views

#Nuestro primer patrón URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]