import json

from django.http import HttpResponse
from django.core import serializers

import sportstore.models as sm


def get_products(request):
    products = serializers.serialize('json', sm.Product.objects.all())

    # FTTB to conform with the book categories as strings (meh), convert our categories into the first category name.
    def transform_product(p):
        return dict(p['fields'].items() +
                    [('id', p['pk']),
                     ('category', sm.Category.objects.get(id=p['fields']['category']).name)])

    products = json.loads(products)
    products = [transform_product(product) for product in products]
    products = json.dumps(products)

    return HttpResponse(products, content_type='application/json')