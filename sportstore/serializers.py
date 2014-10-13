from django.forms import PasswordInput
from rest_framework import serializers

from django.contrib.auth.models import User
import sportstore.models as sm


class CredentialsSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, widget=PasswordInput())
    token = serializers.Field()

    class Meta:
        fields = ('username', 'password', 'token')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, view_name='order-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'orders')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sm.Category
        fields = ('id', 'name', 'product_set')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sm.Product
        fields = ('id', 'name', 'description', 'category', 'price')

    def transform_category(self, obj, category_url):
        """
        Transform the category into its name to follow the book javascript
        :param obj:
        :param value:
        :return:
        """
        if obj and obj.category:
            return obj.category.name


class OrderItemField(serializers.Field):
    def to_native(self, value):
        return [OrderItemSerializer(order_item).data for order_item in value.all()]


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemField(source='orderitem_set')

    class Meta:
        model = sm.Order
        fields = ('id', 'user', 'name', 'street', 'city', 'state', 'zip', 'country', 'giftwrap', 'products')

    def save(self, **kwargs):
        """
        If new, create orderitems
        :param kwargs:
        :return:
        """
        new = self.data['id'] is None
        order = super(OrderSerializer, self).save(**kwargs)
        if new:
            for product_info in self.init_data['products']:
                order_item = sm.OrderItem(
                    order=order,
                    product=sm.Product.objects.get(id=product_info['product_id']),
                    count=product_info['count'],
                    price=product_info['price'])
                order_item.save()
        else:
            raise(Exception('POST update on order object not allowed'))
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('product_name')

    class Meta:
        model = sm.OrderItem
        fields = ('id', 'order', 'product', 'name', 'count', 'price')

    @staticmethod
    def product_name(obj):
        return obj.product.name