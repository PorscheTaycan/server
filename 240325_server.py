import tkinter
from tkinter import filedialog
import socket
from threading import Thread

tk = tkinter.Tk() #메인프레임 선언 new Form()

def send_image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)
def load_csv():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])

def main(x):
    btn = tkinter.Button(tk, text="이미지 불러오기", command=load_csv)
    btn.pack(pady=10)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.31.87', 1111))
    server_socket.listen()
    print('서버 오픈')
    connection,address = server_socket.accept() # 클라이언트가 접속할 때까지 대기
    print("연결클라이언트 주소 : ", address)
    send_image(connection, file_path)
    connection.close()

t = Thread(target=main, args=(1,)) #쓰레드를 생성하고 쓰레드로 rcvMsg() 함수를 구동시키고, 매개변수는 sock객체
t.start()
tk.mainloop()