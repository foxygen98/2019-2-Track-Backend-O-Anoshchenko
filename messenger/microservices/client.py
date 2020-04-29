#! /usr/bin/env python3

import json
import socket
import sys
from pymemcache.client.base import Client
from pymemcache import fallback

def parse_url(url):
    socket_client = socket.socket()
    socket_client.connect(('localhost', 8090))
    url = f'{url}\r\n'
    socket_client.send(url.encode('utf8'))

    data = b''
    tmp = socket_client.recv(1024)
    while tmp:
        data += tmp
        tmp = socket_client.recv(1024)
    url_info = json.loads(data)
    socket_client.close()
    return url_info

def cached(url):
    # result = parse_url(url)
    key = f"{url}"
    result = client.get(key)
    if result is None:
        result = parse_url(url)
        result = json.dumps(result)
        client.set(key, result)
    result = json.loads(result)
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <url>')
        sys.exit(1)

    old_cache = Client(('localhost', 11211), ignore_exc=True)
    new_cache = Client(('localhost', 11212))
    client = fallback.FallbackClient((new_cache, old_cache))
    for i in range(5):
        result = cached(sys.argv[1])
        print(result)
