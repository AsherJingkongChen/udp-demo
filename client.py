#! /usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM

client = socket(AF_INET, SOCK_DGRAM)
client.sendto('This is a test from python client'.encode('utf-8'), ("127.0.0.1", 20213))
print(client.recv(1024).decode('utf-8'))
client.close()
