from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

import sportstore.views as sv

router = DefaultRouter()
router.register(r'users', sv.UserViewSet)
router.register(r'products', sv.ProductViewSet)
router.register(r'categories', sv.CategoryViewSet)
router.register(r'orders', sv.OrderViewSet)
router.register(r'orderitems', sv.OrderItemViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='sportstore/index.html'), name='sportstore'),
    url(r'^admin/$', TemplateView.as_view(template_name='sportstore/admin.html'), name='sportstore_admin'),
    url(r'^api/', include(router.urls)),
    url(r'^get_auth_token/$', sv.GetAuthTokenView.as_view(
        {'get': 'list',
         'post': 'update'}), name='sportstore_get_auth_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')))
