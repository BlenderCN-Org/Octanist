import time
import threading
import socket
import commands

TCP_IP = '127.0.0.1'
TCP_PORT = 5128
BUFFER_SIZE = 1024
SLEEP_RATE = 0.1


def get_new_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock


def socket_update():
    '''
    Socket listener running in thread
    '''
    # First time connection
    try:
        sock = get_new_socket()
        sock.connect((TCP_IP, TCP_PORT))
        connected = True
        print('# Connected to Octanist')
    except socket.error:
        connected = False
        print('! Waiting for socket connection')
        while not connected:
            try:
                sock = get_new_socket()
                sock.connect((TCP_IP, TCP_PORT))
                connected = True                    
                print('# Connected to Octanist')
            except socket.error:
                time.sleep(SLEEP_RATE)

    # Disconnection detection and awaiting for connection
    while(True):
        data = sock.recv(BUFFER_SIZE).decode('utf-8').strip()
        if not data:
            connected = False
            print('! Waiting for socket connection')
            while not connected:
                try:
                    sock = get_new_socket()
                    sock.connect((TCP_IP, TCP_PORT))
                    connected = True
                    print('# Connected to Octanist')
                except socket.error:
                    time.sleep(SLEEP_RATE)
        else:
            print('# Socket Received Data')
            print('- Content: ', data)
            print('- Length: ', len(data))
            commands.commands.get(data, lambda: 'Unknown Command')(sock)
            time.sleep(SLEEP_RATE)

    print('END')


thread_socket = threading.Thread(target=socket_update)
thread_socket.start()
