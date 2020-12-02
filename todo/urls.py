from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.user_update, name='update'),
    path('delete/<int:pk>/', views.user_delete, name='delete')
]
