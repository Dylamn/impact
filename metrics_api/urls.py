from django.urls import path, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from . import views

# router = routers.DefaultRouter()
# router.register(r'reports', views.GenerateReport)

app_name = 'metrics_api'

urlpatterns = [
    path('reports/', views.GenerateReport.as_view(), name='reports.generate'),
]
