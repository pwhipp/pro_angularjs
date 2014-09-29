from django.conf.urls import patterns, url

import sportstore.views as sv

urlpatterns = patterns(
    '',
    url(r'products/$', sv.get_products, name='sportstore_products'))
