from django.http import HttpResponse
from django.core import serializers

import sportstore.models as sm


def get_products(request):
    products = serializers.serialize('json', sm.Product.objects.all())
    return HttpResponse(products, content_type='application/json')