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
    sock = get_new_socket()
    sock.connect((TCP_IP, TCP_PORT))
    connected = True
    print("# Connected to Octanist")

    while(True):
        try:
            # Receive the data as str and strip it
            data = sock.recv(BUFFER_SIZE).decode('utf-8').strip()
            print('# Socket Received Data')
            print('- Content: ', data)
            print('- Length: ', len(data))
            # Send commands to commands lib to execute target command
            commands.commands.get(data, lambda: 'Unknown Command')()

            time.sleep(SLEEP_RATE)
        except socket.error:
            # Try to reconnect when lost connection
            connected = False
            sock = get_new_socket()
            print('! Lost connection to Octanist. Reconnecting...')
            while not connected:
                try:
                    sock.connect((TCP_IP, TCP_PORT))
                    connected = True
                    print("# Connected to Octanist")
                except socket.error:
                    time.sleep(SLEEP_RATE)

thread_socket = threading.Thread(target=socket_update)
thread_socket.start()