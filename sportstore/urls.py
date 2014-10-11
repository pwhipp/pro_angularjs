from django.conf.urls import patterns, url
from django.views.generic import TemplateView

import sportstore.views as sv

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='sportstore/index.html'), name='sportstore'),
    url(r'^admin/$', TemplateView.as_view(template_name='sportstore/admin.html'), name='sportstore_admin'),
    url(r'^products/$', sv.get_products, name='sportstore_products'),
    url(r'^create_order/$', sv.create_order, name='sportstore_create_order'),
    url(r'^get_auth_token/$', sv.get_auth_token, name='sportstore_get_auth_token'))
