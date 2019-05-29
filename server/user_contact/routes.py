from .controllers import (
    add_contact,
    del_contact
)

routes = [
    {'action': 'add_contact', 'controller': add_contact},
    {'action': 'del_contact', 'controller': del_contact},
    {'action': 'get_contacts', 'controller': get_contacts},
]
