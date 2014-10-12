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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = sm.Product
        fields = ('id', 'name', 'description', 'category', 'price')

    def transform_category(self, obj, category_id):
        """
        Transform the category into its name to follow the book javascript
        :param obj:
        :param value:
        :return:
        """
        if category_id:
            return sm.Category.objects.get(id=category_id).name