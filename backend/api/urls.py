from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request),
    path('request/<int:pk>/', views.get_request),
    path('requests/', views.get_all_requests),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
]