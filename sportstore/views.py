import json

from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

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


@csrf_exempt  # TODO: Handle csrf by picking up token in js for posting and remove this exemption
@login_required
def create_order(request):
    """
    Create order and return it as json
    :param request:
    :return:
    """
    order_info = json.loads(request.body)
    order_items_info = order_info.pop('products')

    order = sm.Order(**order_info)
    order.save()

    for order_item_info in order_items_info:
        product = sm.Product.objects.get(id=order_item_info.pop('id'))
        order_item = sm.OrderItem(order=order, product=product, **order_item_info)
        order_item.save()

    order_dict = json.loads(serializers.serialize('json', [order])[1:-1])
    order_dict = dict(order_dict['fields'].items() +
                      [('id', order_dict['pk'])])
    order_json = json.dumps(order_dict)

    return HttpResponse(order_json, content_type='application/json')


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