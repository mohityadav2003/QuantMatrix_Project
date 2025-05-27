from django.urls import path,include
from . import views

urlpatterns = [
    path('filters/', views.filter_options),
    path('dashboard-data/', views.dashboard_data),
]
