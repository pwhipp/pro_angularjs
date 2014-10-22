from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.routers import DefaultRouter

import sportstore.views as sv

# Set up api viewsets
router = DefaultRouter(trailing_slash=False)
router.register(r'users', sv.UserViewSet)
router.register(r'products', sv.ProductViewSet)
router.register(r'categories', sv.CategoryViewSet)
router.register(r'orders', sv.OrderViewSet)
router.register(r'orderitems', sv.OrderItemViewSet)

(sportstore_index_view, sportstore_admin_view) = [
    ensure_csrf_cookie(TemplateView.as_view(template_name=template_name))
    for template_name in ('sportstore/index.html', 'sportstore/admin.html')]

urlpatterns = patterns(
    '',
    url(r'^$', sportstore_index_view, name='sportstore'),
    url(r'^admin/$', sportstore_admin_view, name='sportstore_admin'),
    url(r'^api/', include(router.urls)),
    url(r'^get_auth_token/$', sv.GetAuthTokenView.as_view(
        {'get': 'list',
         'post': 'update'}), name='sportstore_get_auth_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')))
