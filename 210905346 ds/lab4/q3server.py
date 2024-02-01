import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '172.16.59.30'
port = 6666
s.bind((host,port))
while True:
    print("####### Server is listening #######")
    data, recvAddr = s.recvfrom(1024)
    print("Server received: ", data.decode())
    msg = input("Type some text to send =>")
    print("Server sent: ", msg)
    s.sendto(msg.encode(), recvAddr)