import socket
from threading import Thread #동시 처리를 위해 thread 사용
import tkinter #파이썬에 내장 gui 개발 라이브러리
from tkinter import filedialog

tk = tkinter.Tk() #메인프레임 선언 new Form()
tk.geometry("600x800") #해상도 선언
entry = tkinter.Entry(tk, width=30) #텍스트입력 박스 생성
entry2 = tkinter.Entry(tk, width=30) #텍스트입력 박스 생성
entry3 = tkinter.Entry(tk, width=30) #텍스트입력 박스 생성

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def reveive_image(connection, save_path):
    with open(save_path, 'wb') as image_file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            image_file.write(data)


def main():
    label = tkinter.Label(tk, text="이윤서")
    label2 = tkinter.Label(tk, text="HOST")

    label.pack(pady=5)
    label2.pack(pady=5)
    entry.pack(pady=5)
    label3 = tkinter.Label(tk, text="PORT")
    label3.pack(pady=5)
    entry2.pack(pady=5)

    label4 = tkinter.Label(tk, text="저장할 이미지 이름 설정")
    label4.pack(pady=5)
    entry3.pack(pady=5)
    btn = tkinter.Button(tk, text="이미지 저장하기", command=ss)
    btn.pack(pady=10)


    tk.mainloop()
def ss():
    client_socket.connect((entry.get(), int(entry2.get())))

    save_path=entry3.get()+".png"
    reveive_image(client_socket, save_path)
    print("완료")
    client_socket.close()

main()