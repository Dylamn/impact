from django.contrib import admin
from django.urls import include, path

from impact import views

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('terms/', views.TermsView.as_view(), name='terms'),

    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('metrics/', include('metrics.urls')),

    path('api/', include('metrics_api.urls'))
]
