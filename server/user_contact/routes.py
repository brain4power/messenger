from .controllers import (
    add_contact,
    del_contact,
    get_contacts,
    get_all_users,
)

routes = [
    {'action': 'add_contact', 'controller': add_contact},
    {'action': 'del_contact', 'controller': del_contact},
    {'action': 'get_contacts', 'controller': get_contacts},
    {'action': 'get_all_users', 'controller': get_all_users},
]
