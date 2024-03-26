import socket
import threading
import tkinter
from tkinter import filedialog
image_path = ""
def send_image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)

def main(x):
    global image_path
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.31.87", 1111))
    while True:
        server_socket.listen()
        print('서버 오픈')
        connection,address = server_socket.accept() # 클라이언트가 접속할 때까지 대기
        print("연결클라이언트 주소 : ", address)
       # image_path="new_image.jpg"
        send_image(connection, image_path)
        connection.close()
        #server_socket.close()


def btn_click():
    global image_path
    image_path = tkinter.filedialog.askopenfilename(filetypes=[("PNG File", "*.png")])
    print(image_path)
t = threading.Thread(target=main, args=(1,))  #main을 돌리는 쓰레드
t.start()
root = tkinter.Tk()
btn = tkinter.Button(root, text="image", command=btn_click)

btn.pack()
root.mainloop()