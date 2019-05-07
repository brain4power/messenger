import json
import socket
import select
import logging
import threading

from yaml import load, Loader
from argparse import ArgumentParser

from handlers import handle_default_request
import settings

from settings import (
    ENCODING_NAME, HOST,
    PORT, BUFFERSIZE
)

host = HOST
port = PORT
encoding_name = ENCODING_NAME
buffersize = BUFFERSIZE

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)
args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        config = load(file, Loader=Loader)
        host = config.get('host') or HOST
        port = config.get('port') or PORT
        encoding_name = config.get('encoding_name') or ENCODING_NAME
        buffersize = config.get('buffersize') or BUFFERSIZE

handler = logging.FileHandler('main.log', encoding=encoding_name)
error_handler = logging.FileHandler('error.log', encoding=encoding_name)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        handler,
        error_handler,
        logging.StreamHandler(),
    ]
)

requests = []
connections = []


def read_client_data(client, requests, buffersize):
    b_request = client.recv(buffersize)
    requests.append(b_request)


def write_client_data(client):
    client.send(b_response)


try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.settimeout(0)
    sock.listen(5)
    logging.info(f'Server started with { host }:{ port }')

    while True:
        try:
            client, address = sock.accept()
            logging.info(f'Client detected { address }')
            connections.append(client)
        except Exception:
            pass

        rlist, wlist, xlist = select.select(
            connections, connections, connections, 0
        )

        for r_client in rlist:
            thread = threading.Thread(
                target=read_client_data,
                args=(r_client, requests, buffersize)
            )
            thread.start()

        if requests:
            b_request = requests.pop()
            if b_request:
                b_response = handle_default_request(b_request)

                for w_client in wlist:
                    thread = threading.Thread(
                        target=write_client_data,
                        args=(w_client,)
                    )
                    thread.start()

except KeyboardInterrupt:
    logging.info('Server closed')
