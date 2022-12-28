from django.urls import path

from . import views

app_name = 'metrics_api'

urlpatterns = [
    path('reports/', views.GenerateReport.as_view(), name='reports.generate'),
]
