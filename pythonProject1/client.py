import socket # 통신 소켓 TCP/UDP
from threading import Thread # 동시 처리를 위해 thread 사용
import tkinter # 파이썬 내장 GUI 개발 라이브러리
tk = tkinter.Tk() #메인 프레임 선언
tk.geometry("1000x1000") # 해상도 선언
entry = tkinter.Entry(tk) # 텍스트입력 박스 생성
entry2 = tkinter.Listbox(tk, height=15, width=50) #대화창 목록 리스트박스 (사이즈 설정) 생성


HOST = '192.168.31.87'    # 내가 접속할 서버의 ip주소
# LOCALHOST : 내 로컬 환경 ip를 의미
# 127.0.0.1 : 내 로컬 환경 ip를 의미

PORT = 9900        # 서버의 포트 번호 (서로 같아야 연결 가능)
def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
            entry2.insert(-1,data.decode()+"\n")
            entry2.update()
            entry2.see(0)
        except:
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True#데몬스레드로 설정해서 메인스레드가 종료되면 자동으로 함꼐 종료, 프로세스 묶이는 문제 방지
        t.start()

        def okClick():
            sock.send(entry.get().encode())

        def onEnter(event):
            okClick()
            entry.delete(0,tkinter.END)

        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
        label = tkinter.Label(tk, text="채팅.")
        entry.pack()
        label.pack()
        btn = tkinter.Button(tk, text="OK", command=okClick)
        btn.pack()
        entry.bind("<Return>", onEnter)
        tk.mainloop()

runChat()