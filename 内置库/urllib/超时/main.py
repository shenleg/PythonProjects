import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

