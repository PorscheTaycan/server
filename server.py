import socket #통신 소켓 tcp/udp
from threading import Thread #동시 처리를 위해 thread 사용
import tkinter #파이썬에 내장 gui 개발 라이브러리

#0.퇴장, 입장, 채팅창 얼리기 and 풀기 : 회색 / 공지 : 파란색 / 강퇴 : 빨간색 / 귓속말 : 노랑
#1.listbox에서 상대에게 온 귓속말 텍스트를 누르면 자동으로 entry에 답장모드로 전환[/w 보낸사람]로 전환
#2.클라이언트 접속종료 버튼
#3.관리자는 권한으로
# 강퇴/강퇴해제(entry에 대상 인원 이름 or IP를 입력하고 버튼으로 강퇴/ 강퇴해제),
# 얼리기/채팅창 풀기 : 버튼으로 만든다.
# 공지 : entry 만들고 공지멘트 입력후 '공지' 버튼 누르면 공지사항 발송


#4.현재 채팅방 접속자 목록과 총 인원
#   레이아웃 우측 하단에 listbox와 라벨
#   수의 변화를 감지하는 쓰레드 필요
#5.4에서 만든 접속자 목록 중 특정인원 클릭하면 귓속말 커맨드가 entry 자동입력되고 /w 대상 뒤에 커서 포커스 잡힘



tk = tkinter.Tk() #메인프레임 선언 new Form()
tk.geometry("600x800") #해상도 선언
stringv = tkinter.StringVar()
stringv2 = tkinter.StringVar()
entry = tkinter.Entry(tk, textvariable=stringv) #텍스트입력 박스 생성
entry2 = tkinter.Listbox(tk, height=10, width=50) #대화창 목록 리스트박스 생성
entry3 = tkinter.Entry(tk, width=20)
entry4 = tkinter.Listbox(tk, height=10, width=30)
entry5 = tkinter.Entry(tk,width=20)


HOST = '192.168.31.87'    # 내가 접속할 서버의 ip주소
#localhost : 내 로컬 환경 ip를 의미
#127.0.0.1 : 내 로컬 환경 ip를 의미

PORT = 9900     # 서버의 포트 번호 (서로 같아야 연결 가능)


def get_selection(event):
    global stringv
    try:
        idx = entry2.curselection()[0]
        value = entry2.get(idx)
        splitValue = value.split()
        if splitValue[1] == ">>>":  # entry.icursor(tkinter.END)
            entry.delete(0, tkinter.END)
            stringv.set("/w "+splitValue[0]+" ")
            entry.icursor(len(entry.get())+1)
            tk.after(1, entry.focus_set)
    except Exception as e:
        print(e)
def get_selection2(event):
    global stringv
    try:
        idx = entry4.curselection()[0]
        value = entry4.get(idx)
        entry.delete(0, tkinter.END)
        stringv.set("/w "+value+" ")
        entry.icursor(len(entry.get())+1)
        tk.after(1, entry.focus_set)
    except Exception as e:
        print(e)
def rcvMsg(sock):
    while True: #무한루프
        try:
            data = sock.recv(1024) #1024 단위로 자른 데이터를 받는다

            if " " in data.decode():
                splitData = data.decode().split()
            color = ["red", "blue", "grey", "green"]
            if data:
                if splitData[1] == ">>>" or splitData[1] == "<<<":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0,{'fg':color[3]})
                elif splitData[0] == "[전체공지]":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[1]})
                elif splitData[1] == "입장" or splitData[1] == "퇴장." or splitData[0] == "채팅이":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[2]})
                elif splitData[1] == "강제퇴장":#강제퇴장 메세지 받은 경우
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[0]})
                elif splitData[0] == "^^":#실시간 접속 명부 데이터임
                    entry4.delete(0, tkinter.END)
                    for i in range(1,len(splitData)):
                        entry4.insert(-1,   splitData[i] + "\n")
                else:#일반 메세지

                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': 'black'})
                entry2.update()
                entry2.see(0) #0번째 관점을 가지겠다.
                entry4.update()
                entry4.see(0)
        except:
            tk.destroy()
            pass



def runChat():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #소켓 객체 sock 생성
            sock.connect((HOST, PORT)) #소켓을 통해 connect 메서드 호출
            t = Thread(target=rcvMsg, args=(sock,)) #쓰레드를 생성하고 쓰레드로 rcvMsg() 함수를 구동시키고, 매개변수는 sock객체
            t.daemon = True #데몬스레드로 설정해서 메인스레드가 종료되면 자동으로 함꼐 종료, 프로세스 묶이는 문제 방지
            t.start()
            def okClick():
                sock.send(entry.get().encode())
            def onEnter(event):
                okClick()
                entry.delete(0, tkinter.END) #entry 박스 값을 소켓에 인코딩후 전송
            def out():
                tk.destroy()
            def forced_exit_Clinck():
                sock.send(("/o "+entry3.get()).encode())
            def forced_exit_lifted_Clinck():
                sock.send(("/i "+entry3.get()).encode())
            def btn_enable_chat_Clinck():
                sock.send("/b".encode())
            def btn_notice_chat_Clinck():
                sock.send(("/n "+entry5.get()).encode())
            entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
            label = tkinter.Label(tk, text="채팅.")
            entry.pack()
            label.pack()
            btn = tkinter.Button(tk, text="OK", command=okClick)
            btn.pack()
            entry.bind("<Return>", onEnter)
            entry2.bind("<<ListboxSelect>>", get_selection)
            entry4.bind("<<ListboxSelect>>", get_selection2)
            btn_out = tkinter.Button(tk, command=out, text="나가기", pady=5)
            btn_out.pack(pady=5)
            entry3.pack(pady=5)
            btn_forced_exit = tkinter.Button(tk, text="강제퇴장",command=forced_exit_Clinck)
            btn_forced_exit.pack(pady=5)
            btn_forced_exit_lifted = tkinter.Button(tk, text="강제퇴장 해제", command=forced_exit_lifted_Clinck)
            btn_forced_exit_lifted.pack(pady=5)
            btn_enable_chat = tkinter.Button(tk, text="채팅 활성화/비활성화",command=btn_enable_chat_Clinck)
            btn_enable_chat.pack(pady=5)
            btn_notice_chat = tkinter.Button(tk,text="공지하기",command=btn_notice_chat_Clinck)
            entry5.pack()
            btn_notice_chat.pack()
            entry4.pack(side=tkinter.BOTTOM,pady=50)
            tk.mainloop() #mainloop 위에서 만든 tk_form을 구동시킨다
            #mainloop는 스레드 점유한다.
    except Exception:
        pass



runChat()