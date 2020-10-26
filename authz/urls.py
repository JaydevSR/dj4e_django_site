from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'authz'

urlpatterns = [
            path('', TemplateView.as_view(template_name='authz/main.html')),
            path('open', views.OpenView.as_view(), name='open'),
            path('apereo', views.ApereoView.as_view(), name='apereo'),
            path('manual', views.ManualProtect.as_view(), name='manual'),
            path('protect', views.ProtectView.as_view(), name='protect'),
            path('python', views.DumpPython.as_view(), name='python'),
        ]
