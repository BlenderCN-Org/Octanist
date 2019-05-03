import time
import threading
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5201
BUFFER_SIZE = 1024
SLEEP_RATE = 0.1
SOCK = None
SUCCESS_RES = {
    "type": "sys",
    "code": "client_connected"
}

# Socket Client


def get_new_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock


def socket_update():
    '''
    Socket listener running in thread
    '''
    global SOCK
    # First time connection
    try:
        sock = get_new_socket()
        sock.connect((TCP_IP, TCP_PORT))
        connected = True
        print('# Connected to Octanist')
        SOCK = sock
        send(SUCCESS_RES)
    except socket.error:
        connected = False
        SOCK = None
        print('! Waiting for socket connection')
        while not connected:
            try:
                sock = get_new_socket()
                sock.connect((TCP_IP, TCP_PORT))
                connected = True
                print('# Connected to Octanist')
                SOCK = sock
                send(SUCCESS_RES)
            except socket.error:
                time.sleep(SLEEP_RATE)

    # Disconnection detection and awaiting for connection
    while(True):
        data = sock.recv(BUFFER_SIZE).decode('utf-8').strip()
        if not data:
            connected = False
            SOCK = None
            print('! Waiting for socket connection')
            while not connected:
                try:
                    sock = get_new_socket()
                    sock.connect((TCP_IP, TCP_PORT))
                    connected = True
                    print('# Connected to Octanist')
                    SOCK = sock
                    send(SUCCESS_RES)
                except socket.error:
                    time.sleep(SLEEP_RATE)
        else:
            print('# Socket Received Data')
            print('- Content: \n', data)
            time.sleep(SLEEP_RATE)


def send(res=None):
    while(SOCK == None):
        time.sleep(SLEEP_RATE)
    if(res != None):
        SOCK.send(bytes(str(res), 'utf-8'))


def connect():
    thread_socket = threading.Thread(target=socket_update)
    thread_send = threading.Thread(target=send)
    thread_socket.start()
    thread_send.start()

# Communications
