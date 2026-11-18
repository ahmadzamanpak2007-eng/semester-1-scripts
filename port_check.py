import socket

target = "127.0.0.1"
ports = [22, 80, 443, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    status = "OPEN" if result == 0 else "CLOSED"
    print(f"Port {port}: {status}")
    sock.close()