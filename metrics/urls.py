from django.urls import path

from . import views

app_name = 'metrics'

urlpatterns = [
    path('run/', views.MetricsView.as_view(), name='run'),
    path('results/', views.MetricsView.as_view(), name='results'),
]