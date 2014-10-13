"""
Using Django rest framework we supply a full API for the sportstore which
supports CSRF protection and proper authentication.
"""
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from rest_framework import viewsets

from django.contrib.auth.models import User

import sportstore.serializers as serializers
import sportstore.models as sm


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = sm.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = sm.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = sm.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
        super(OrderViewSet, self).pre_save(obj)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = sm.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


def get_auth_token(request):
    """
    Supply an authentication token if the username/password is valid (otherwise raise 403 forbidden)
    :param request:
    :return:
    """
    try:
        username, password = (request.POST[varname] for varname in ('username', 'password'))
    except KeyError:
        return HttpResponse('Parameters incorrect', status_code=400)

    user = authenticate(username=username, password=password)
    if user:
        login(request._request, user)
        return
    else:
        return HttpResponse('Credentials invalid', status_code=403)