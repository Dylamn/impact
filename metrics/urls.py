from django.urls import path

from . import views

app_name = 'metrics'

urlpatterns = [
    path('run/', views.run, name='run'),

    path(
        'compare/<uuid:actual_report_uuid>/<uuid:previous_report_uuid>',
        views.compare_reports,
        name='compare'
    ),

    path('results/<uuid:pk>', views.ReportView.as_view(), name='results'),
    path(
        'results/<uuid:pk>/<section>/<metric>',
        views.ReportView.as_view(),
        name='results'
    ),

    path('', views.ReportListView.as_view(), name='reports'),
]
