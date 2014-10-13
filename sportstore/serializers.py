from rest_framework import serializers

from django.contrib.auth.models import User
import sportstore.models as sm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #orders = serializers.HyperlinkedRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username')


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
        if obj.category:
            return obj.category.name


class OrderItemField(serializers.WritableField):
    def to_native(self, value):
        return [OrderItemSerializer(order_item).data for order_item in value.all()]

    def field_from_native(self, data, files, field_name, into):
        import pdb; pdb.set_trace()
        super(OrderItemField, self).field_from_native(data, files, field_name, into)


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemField(source='orderitem_set')

    class Meta:
        model = sm.Order
        fields = ('id', 'name', 'street', 'city', 'state', 'zip', 'country', 'giftwrap', 'products')


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('product_name')

    class Meta:
        model = sm.OrderItem
        fields = ('id', 'order', 'product', 'name', 'count', 'price')

    @staticmethod
    def product_name(obj):
        return obj.product.name