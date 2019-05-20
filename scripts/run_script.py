import subprocess
from threading import Thread


def run_read_client():
    run_read_client = subprocess.call(['python3 ../client/ -m r', '-i'], shell=True)


def run_write_client():
    run_write_client = subprocess.call(['python3 ../client/ -m w', '-i'], shell=True)


number_of_read_client = input('Сколько клиентов на чтение запустить: ')

clients = []

for i in range(int(number_of_read_client)):
    subprc = Thread(target=run_read_client)
    clients.append(subprc)

for each in clients:
    each.start()

for each in clients:
    each.join()
