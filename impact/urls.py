from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from impact import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),

    path('api/', include('metrics_api.urls'))
]

urlpatterns += i18n_patterns(
    path('', views.LandingView.as_view(), name='landing'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('', include('accounts.urls')),
    path('metrics/', include('metrics.urls')),
)
