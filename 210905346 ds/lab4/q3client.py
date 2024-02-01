import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '172.16.59.30'
port = 6666
while True:
    msg = input("Type some text to send =>")
    print("Client sent: ", msg)
    s.sendto(msg.encode(),(host,port))
    rcv_msg, serAddr = s.recvfrom(1024)
    print("Client received: ", rcv_msg.decode())