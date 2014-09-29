from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

import todo.urls
import jsdemo.urls

urlpatterns = patterns(
    '',
    url(r'todo/', include(todo.urls)),
    url(r'jsdemo/', include(jsdemo.urls)),
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name='home'),
    url(r'^test/$', TemplateView.as_view(template_name='core/test.html'), name='test'),
    url(r'^admin/', include(admin.site.urls)))
