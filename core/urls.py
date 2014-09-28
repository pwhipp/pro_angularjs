from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^test/', TemplateView.as_view(template_name='core/test.html')),
    url(r'^admin/', include(admin.site.urls)))
