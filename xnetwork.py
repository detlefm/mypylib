import socket
import struct


def ip2url(ip_addr:str,port:int=0) ->str:
    url = f'http://{ip_addr}'
    if port > 0:
        url =  url + f':{port}'
    return url



def wol(mac_address:str):
    # from https://github.com/LouisJin/WakeOnLan-Python
    mac_address_fmt = mac_address.replace('-', '').replace(':', '')
    host_ip = socket.gethostbyname(socket.gethostname())
    host = (host_ip[: host_ip.rindex('.') + 1] + '255', 9)
    data = ''.join(['FFFFFFFFFFFF', mac_address_fmt * 16])
    send_data = b''

    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    rw = sock.sendto(send_data, host)
    return rw    




def isup(ipaddr:str,port:int,timeout:int=1) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((ipaddr, port))
        return result==0


