import socket

HOST = '127.0.0.1'  
PORT = 65433       
FILENAME = 'file_to_send.txt'  





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    with open(FILENAME, 'rb') as file:
        client_socket.sendfile(file)




print(f"[+] File '{FILENAME}' successfully sent to the server.")
