import dis
import socket


class ClientVerifier(type):
    def __init__(self, cls_name, bases, cls_dict):
        for key, value in cls_dict.items():
            assert not isinstance(value, socket.socket), 'Запрещено создавать сокет на уровне класса'

            try:
                instructions = dis.get_instructions(value)
            except TypeError:
                continue
            if instructions:
                for el in instructions:
                    assert not el.argval == 'accept' or not el.argval == 'listen', \
                        'Запрещено вызывать accept и listen для сокетов'

                    if el.opname == 'LOAD_ATTR':
                        assert not el.argval == 'SOCK_DGRAM', 'Запрещено использовать сокеты для UDP'
        type.__init__(self, cls_name, bases, cls_dict)
