"""
Using Django rest framework we supply a full API for the sportstore which
supports CSRF protection and proper authentication.
"""
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token as AuthToken
from rest_framework.response import Response
from rest_framework import status as rs

from django.contrib.auth.models import User

import sportstore.serializers as serializers
import sportstore.models as sm
from sportstore.permissions import IsOwnerOrAdmin


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = sm.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = sm.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrAdmin,)
    queryset = sm.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def pre_save(self, obj):
        obj.user = self.request.user
        super(OrderViewSet, self).pre_save(obj)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = sm.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer




class GetAuthTokenView(viewsets.GenericViewSet):
    """
    Requires user credentials (POST) or user logged in via session to
    GET.
    Supplies username/password (empty)/token
    """
    serializer_class = serializers.CredentialsSerializer
    permission_classes = ()

    def get_object(self):
        user = self.request.user
        if user.is_authenticated():
            try:
                created = False
                token = user.auth_token.key
            except AuthToken.DoesNotExist:
                # Create one
                auth_token = AuthToken(user=user)
                auth_token.save()
                created = True
                token = auth_token.key
            return (dict(username=user.username,
                         password='', # for consistency
                         token=token),
                    created)
        else:
            return (dict(username="",
                         password="",
                         token=""),
                    False)

    def get_response(self):
        (obj, created) = self.get_object()
        if created:
            return_status = rs.HTTP_201_CREATED
        else:
            return_status = rs.HTTP_200_OK
        serializer = serializers.CredentialsSerializer(obj)
        return Response(serializer.data, status=return_status)

    def update(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.DATA)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data['username'],
                password=serializer.data['password'])
            self.request.user = user
            if user:
                login(self.request._request, user)
                return self.get_response()
            else:
                return Response("Credentials invalid", status=rs.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=rs.HTTP_400_BAD_REQUEST)

    def list(self, *args, **kwargs):
        return self.get_response()