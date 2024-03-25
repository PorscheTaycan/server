import socket
import os

def send_image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 1111))
    server_socket.listen()
    print('서버 오픈')
    connection,address = server_socket.accept() # 클라이언트가 접속할 때까지 대기
    print("연결클라이언트 주소 : ", address)
    image_path="new_image.jpg"
    send_image(connection, image_path)
    connection.close()
    server_socket.close()

if __name__=="__main__":
    main()