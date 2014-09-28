from django.conf.urls import patterns, url

from django.views.generic import TemplateView

import todo.views as tv

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='todo/todo.html'), name='todo'),
    url(r'items/$', tv.get_todo_items, name='todo_items'))
