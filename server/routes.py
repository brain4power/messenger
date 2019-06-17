from functools import reduce
from settings import INSTALLED_MODULES
from pprint import pprint


def get_server_routes():
    return reduce(
        lambda value, item: value + [getattr(item, 'routes', None)],
        reduce(
            lambda value, item: value + [getattr(item, 'routes', None)],
            reduce(
                lambda value, item: value + [__import__(f'{ item }.routes')],
                INSTALLED_MODULES,
                []
            ),
            []
        ),
        []
    )


def resolve(action, routes=None):
    routes_mapping = {}
    for route in routes or get_server_routes():
        for sub_route in route:
            routes_mapping[sub_route['action']] = sub_route['controller']
    return routes_mapping.get(action, None)
