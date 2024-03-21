import socket # 통신 소켓 TCP/UDP
from threading import Thread # 동시 처리를 위해 thread 사용
import tkinter # 파이썬 내장 GUI 개발 라이브러리
import random
#tkinter.Canvas
#tkinter.Entry
#tkinter.Label
#tkinter.Button
#tkinter.Frame


tk = tkinter.Tk() #메인 프레임 선언 new From()만드는 것 처럼 만드는 것임.
tk.geometry("1000x1000") # 해상도 선언

entry = tkinter.Entry(tk) # 텍스트입력 박스 생성 #entry식별자에 tkinter에서 제공하는 Entry (텍스트입력상자) thinter Form에다가 올리겠다.
entry2 = tkinter.Listbox(tk, height=15, width=50) #대화창 목록 리스트박스 (사이즈 설정) 생성



HOST = '192.168.31.87'    # 내가 접속할 서버의 ip주소
# LOCALHOST : 내 로컬 환경 ip를 의미
# 127.0.0.1 : 내 로컬 환경 ip를 의미

PORT = 9900        # 서버의 포트 번호 (서로 같아야 연결 가능)
def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            print(data, "ㅇㅇㅇㅇㅇㅇㅇㅇ")
            data1 = []
            if not data:
                break
            print(data.decode())
            entry2.insert(-1,data.decode()+"\n") # 대화가 맨 뒤에 추가가 되겠다.
            data1.append(data.decode())
            if data.decode().startswith('공지사항'):
                print("ddddddd")
            #entry2.itemconfig(0, {'fg' : 'red'})
            entry2.update() # update와 insert가 같이 쓰여야 업데이트가 되어서 대화 추가가 된 것을 반영 시켜준다. #인서트 결과 반영
            entry2.see(0) # 맨 위에 내용을 봐야하니까 0번째의 값이 포거스가 되는 것

        except:
            tk.destroy() # form1.dispose() # form1.close() 와 같은 역할
            pass


#stringv = tkinter.StringVar()
def runChat():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True#데몬스레드로 설정해서 메인스레드가 종료되면 자동으로 함꼐 종료, 프로세스 묶이는 문제 방지
        t.start()


        def okClick():
            sock.send(entry.get().encode()) # 텍스트를 가져와서 encode해서 socket으로 보내겠다. # entry박스 값을 소켓에 인코딩 후 전송

        def onEnter(event):
            okClick()
            entry.delete(0,tkinter.END) # 0부터 끝까지 # entry박스 값 지우기

        def out():
            tk.destroy()

        def get_selection(event):
            global stringv

            try:
                index = entry2.curselection()[0]  # 튜플로 리턴 오기때문에 인덱싱0번
                value = entry2.get(index)
                stringv.set("/w " + value[0]+value[1]+value[2] + " ")
                entry.icursor(len(entry.get()))
                tk.after(1, entry.focus_set)  # after는 1이라는 지연시간
            except:
                pass


        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5) # 사이드 방향 왼쪽 fill 채우기 padx -> 패딩 x축, pady -> 패딩 y축
        # pack함수 : 배치를 위한 함수

        label = tkinter.Label(tk, text="채팅.")
        entry.pack() # 위에서부터 차곡차곡 만들어진다.
        label.pack()
        btn = tkinter.Button(tk, text="OK", command=okClick)
        btn.pack()
        btn2 = tkinter.Button(tk, text="종료하기", command=out)
        btn2.pack()
        entry.bind("<Return>", onEnter) # 이벤트에 등록하는 것이 bind 행위 # return키는 엔터키를 의미
        entry2.bind("<<ListboxSelect>>", get_selection)

        tk.mainloop() # mainloop 위에서 만든 tk_form을 구동시킨다.
        #mainloop는 스레드 점유한다.
        print("123") #-> mainloop에 갇혀서 123은 절대 실행될 수 없다.

runChat()


