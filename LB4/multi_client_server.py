import socket


HOST = '127.0.0.1'  
PORT = 65432        





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[*] Multi-client server is running on {HOST}:{PORT}")
    

    
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Connected to {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
