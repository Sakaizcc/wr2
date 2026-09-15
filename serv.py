import socket,sys

def server(ip: str, port: int):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((ip, port))
        server_socket.listen(1)
        #print(f"Server listening on {ip}:{port}...")

        connection, client_address = server_socket.accept()
        #print(f"Connected to client at {client_address}")
        
        try:
            data = connection.recv(1024)
            if data:
                return (f"Received data: {data.decode('utf-8')}")
        finally:
            connection.close()
            
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
ip = ''
port = 0
sfile = ''
args = sys.argv[1:]
i = 0

while i < len(args):

    arg = args[i]

    if arg.startswith("-"):

        option = arg.strip("-").lower()

        if option == "op":
            print("OPTIONS:")
            print("-ip for IP [serv -ip \"0.0.0.0\"]")
            print("-p for port [serv -ip \"0.0.0.0\" -p 67]")
            sys.exit()
        elif option == "ip":
            if i + 1 < len(args):
                ip = args[i + 1]
                i += 1
        elif option == "p":
            if i + 1 < len(args):
                try:
                    port = int(args[i + 1])
                    i += 1
                except ValueError:
                    print("Port must be an integer")
                    sys.exit(1)
        elif option == 's':
            if(i+1 < len(args)):
                sfile = args[i + 1]
        else:
            print(f"Unknown option: {arg}")
            sys.exit(1)

    i += 1


if not ip:
    print("IP is required")
    sys.exit(1)

if port == 0:
    print("Port is required")
    sys.exit(1)
def op(fname ,data):
    with open(fname ,"w")as f:
        f.write(data)
        return

print(server(ip, port))