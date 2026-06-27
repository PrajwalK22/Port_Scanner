import socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
while True:
    data, addr = s.recvfrom(65535)
    if data[23] == 6 and data[12:14].hex() == '0800':
        print("Source Port:", int.from_bytes(data[34:36], 'big'))
        print("Dest Port:", int.from_bytes(data[36:38], 'big'))
        print("Destination MAC:", data[0:6].hex())
        print("Source MAC:", data[6:12].hex())
        print("EthernetType:", data[12:14].hex())
        print("IP Version:", data[14] >> 4)
        print("Protocol:", data[23])
        print("SourceIP:", str(data[26]) + "." + str(data[27]) + "." + str(data[28]) + "." + str(data[29]))
        print("DestIP:", str(data[30]) + "." + str(data[31]) + "." + str(data[32]) + "." + str(data[33]))
        if data[47] == 2:
            print("TCP Flag: SYN")
        if data[47] == 18:
            print("TCP Flag: SYN-ACK")
        if data[47] == 4:
            print("TCP Flag: RST")
        if data[47] == 16:
            print("TCP Flag: ACK")
        if data[47] == 1:
            print("TCP Flag: FIN")
        print("---")
