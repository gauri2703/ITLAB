import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12345
# For UDP
# Host IP
# specified port to connect
sock.bind((udp_host, udp_port))
while True:
    print('Waiting for client...')
    data,addr = sock.recvfrom(1024)
#receive data from client
    print('Received Messages:',data.decode(),'from',addr)
sock.close()