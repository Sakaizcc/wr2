#
#GNG I SADLY DELETED THE PYTHON FILE BUT STILL HAVE THE .exe file for send.py but I tried recreating it
#
import socket,sys

prtcls = ['tcp','udp']

args = sys.argv

def send(ip: str, data: str, port: int, times: int, protocol: str = 'tcp', show: bool = False):

    if protocol not in prtcls:
        raise NameError

    for i in range(times):

        if protocol == 'tcp':
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((ip,port))
            sock.send(data.encode())

        elif protocol == 'udp':
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.sendto(data.encode(),(ip,port))

        else:
            raise NameError

        if show:
            print(i + 1)

        sock.close()


ip = None
data = None
port = None
times = 1
protocol = 'tcp'
show = False

i = 1

while i < len(args):

    if args[i] == '-ip':
        ip = args[i + 1]
        i += 2

    elif args[i] == '-d':
        data = args[i + 1]
        i += 2

    elif args[i] == '-p':
        port = int(args[i + 1])
        i += 2

    elif args[i] == '-t':
        times = int(args[i + 1])
        i += 2

    elif args[i] == '-pr':
        protocol = args[i + 1].lower()
        i += 2

    elif args[i] == '-pv':
        print('TCP')
        print('UDP')
        i += 1

    elif args[i] == '-s':
        show = True
        i += 1

    else:
        i += 1

if ip is not None and data is not None and port is not None:
    send(ip,data,port,times,protocol,show)
