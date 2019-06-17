from datetime import datetime
import json
import socket
from yaml import load, Loader
from argparse import ArgumentParser

from routes import resolve
from protocol import (
    validate_request, make_response,
    make_400, make_404
)
from settings import (
    ENCODING_NAME, VARIABLE, HOST,
    PORT, BUFFERSIZE
)

from verifiers.client_verifier import ClientVerifier

host = HOST
port = PORT
encoding_name = ENCODING_NAME
buffersize = BUFFERSIZE

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)
parser.add_argument(
    '-m', '--mode', type=str, default='w'
)
args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        config = load(file, Loader=Loader)
        host = config.get('host') or HOST
        port = config.get('port') or PORT
        encoding_name = config.get('encoding_name') or ENCODING_NAME
        buffersize = config.get('buffersize') or BUFFERSIZE


class Client(metaclass=ClientVerifier):
    def __init__(self, host, port, buffersize):
        self.host = host
        self.port = port
        self.buffersize = buffersize

    def run_client(self):
        try:
            sock = socket.socket()
            sock.connect((self.host, self.port))
            print(f'Client started with { self.host }:{ self.port }')

            if args.mode == 'w':

                while True:
                    value = input('Enter data to send:')
                    response = {
                        'action': 'get_all_users',
                        'time': datetime.now().timestamp(),
                        'data': value
                    }
                    s_response = json.dumps(response)
                    b_response = s_response.encode(encoding_name)
                    sock.send(b_response)

            else:
                while True:
                    data = sock.recv(self.buffersize)
                    print(data.decode(encoding_name))
        except KeyboardInterrupt:
            print('Client closed')


if __name__ == '__main__':
    client = Client(host, port, buffersize)
    client.run_client()
