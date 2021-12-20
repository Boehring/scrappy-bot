from json import JSONDecodeError

import requests


def get_road_articles():
    payload = {'merchComponent': 317848, 'category': 46522, 'route[id]': 46522, 'route[name]': 'equipacion-moto',
               'route[prefix]': 'c', '_componentType': 'product_list_elastic', 'page': 1, '_limit': '65000'}
    return make_request(payload)


def get_helmets():
    payload = {'merchComponent': 345729, 'category': 46530, 'route[id]': 46530, 'route[name]': 'cascos-integrales',
               'route[prefix]': 'c', '_componentType': 'product_list_elastic', 'page': 1, '_limit': '65000'}
    return make_request(payload)


def make_request(payload):
    result = requests.get('https://www.motoblouz.es/api/products/list/data', params=payload)
    return result.json()


def get_product_detail(product_id):
    result = requests.get('https://www.motoblouz.es/api/products/{}'.format(product_id))
    return result.json()


def get_product_prices(product_id):
    result = requests.get('https://www.motoblouz.es/api/product_prices/{}'.format(product_id))
    try:
        return result.json()
    except JSONDecodeError:
        return None
