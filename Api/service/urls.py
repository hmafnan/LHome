from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bookings, name='bookings'),
    path('<str:email>', views.get_booking, name='booking'),
    path('create/', views.create_booking, name='create'),
    path('delete/<str:pk>', views.delete_booking, name='delete'),
]
