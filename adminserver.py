import socketserver
import threading
import time



HOST = '192.168.31.87'
PORT = 9900
lock = threading.Lock()
user_list = ["김중규", "정재현", "허민재", "이윤서", "윤하얀", "전중용", "윤석현", "박희창", "진정현", "김지욱", "성재민", "강병헌", "김자연", "김영기"]
admin = ["admin"]
class UserManager:
    slang_list = []

    def __init__(self):
        self.users = {} #client side를 통해 접속한 유저 객체를 담는 변수
        self.per = True
        self.block_list = []
        self.block_ip_list = []
    def get_txt(self):
        try:
            with open('Slang.txt', 'r', encoding='utf-8') as f:
                self.slang_read = f.read()
                self.slang_list = self.slang_read.split(",")

        except:
            pass
    def sendUserList(self):
        pass

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('already exist.\n'.encode())
            return None
        lock.acquire() #thread의 lock객체는 공유데이터를 다룰 때 스레드를 독립성을 보장
        self.users[username] = (conn, addr)  # 이사이에는 동기화 되어야 하는 작업이 들어가야한다.
        lock.release() #독립성 보장해야하는 작업이 끝나면 release로 풀어줌
        self.sendMessageToAll('[%s] 입장' % username)
        self.user_list_str = "^^"#실시간 접속자 목록을 담은 문자열을 첫글자 ^^로 시작해서 만드는 변수
        for key in self.users.keys():
            #실시간 self.users 딕셔너리에서 사용자 이름만 뜯어서 문자열로 만드는과정
            self.user_list_str += " "+key
        self.sendMessageToAll(self.user_list_str)
        #모든 접속 중인 클라이언트 객체들에게 위에서 만든 명부 문자열을 송출하는 함수 호출
        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 퇴장.' % username)
        self.user_list_str = "^^"
        for key in self.users.keys():
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)
    def forced_exit(self, username):
        if username not in self.users:
            return
        self.users[username][0].close()
        user_list.remove(username)
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 강제퇴장 당하셨습니다.' % username)
        self.user_list_str = "^^"
        for key in self.users.keys():
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)
    def messgeBlock(self, tagetName):
        print(tagetName, self.block_list)
        for i in range(len(self.block_list)):
            print(tagetName, self.block_list[i])
            if tagetName == self.block_list[i]:
                return 1
        for i in range(len(self.block_list)):
            print(tagetName, self.block_list[i])
            if self.users[tagetName][1][0] == self.block_list[i]:
                return 1
        else:
            return
    def messageHandler(self, username, msg): #강퇴하기나 이런 명령 여기서 하기
        try:
            splMsg = msg.split()
            self.get_txt()
            if msg[0] != '/' and self.per:
                for i in range(len(self.slang_list)):
                    if self.slang_list[i] in msg and self.per:
                        self.sendMessageToAll('[%s] %s' % (username, "욕하지마!"))
                        return
                    if i==len(self.slang_list)-1:
                        self.sendMessageToAll('[%s] %s' % (username, msg))
                        return
            else:
                if splMsg[0] == "/o" and username == "admin":
                    self.name = splMsg[1]
                    self.forced_exit(self.name)
                    print(self.name)
                elif splMsg[0] == "/b" and username == "admin":
                    if (self.per):
                        self.per = False
                        self.sendMessageToAll("채팅이 비활성화 됩니다.")
                        return
                    elif (self.per == False):
                        self.per = True
                        self.sendMessageToAll("채팅이 활성화 됩니다.")
                        return
                elif splMsg[0] == "/n" and username == "admin" and self.per:
                    tmp = msg.strip('/n')
                    print(tmp)
                    self.sendMessageToAll('%s %s' % ("[전체공지]", tmp))
                    return

                elif splMsg[0] == "/i" and username == "admin":
                    self.name = splMsg[1]
                    if self.name not in user_list:
                        user_list.append(self.name)
                    print(self.name)

                elif splMsg[0] == "/w":
                    self.name = splMsg[1]
                    if self.name in user_list or self.name in admin:
                        tmp = msg.split()
                        str1 = self.name + " <<< "
                        str2 = username + " >>> "
                        for i in range(2, len(tmp)):
                            str1 += tmp[i]+ " "
                            str2 += tmp[i]+ " "
                        self.sendMessageWhisper1(username, str1)

                        if self.messgeBlock(username) == 1:
                            self.users[username][0].send("차단당했습니다.".encode())
                            return
                        else:
                            self.sendMessageWhisper2(self.name, str2)
                            return
                    else:
                        self.users[username][0].send("잘못된 유저에게 전송 시도 하였습니다.".encode())
                        return
                elif splMsg[0] == "/차단":
                    self.name = splMsg[1]
                    self.block_list.append(self.name)
                elif splMsg[0] == "/차단해제":
                    self.name = splMsg[1]
                    self.block_list.remove(self.name)
            if msg.strip() == '/quit':
                self.removeUser(username)
                return -1
        except Exception as e:
            print(e)

    def sendMessageWhisper1(self, Sender_username, msg):
        try:
            self.users[Sender_username][0].send(msg.encode())
        except Exception as e:
            print(e)
    def sendMessageWhisper2(self, taget_username, msg):
        try:
            self.users[taget_username][0].send(msg.encode())
        except Exception as e:
            print(e)
    def sendMessageToAll(self, msg):
        try:
            for conn, addr in self.users.values():
                conn.send(msg.encode())
        except Exception as e:
            print(e)


class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()
    def handle(self):
        print(self,"self memory")
        print('client [%s] 연결' % self.client_address[0])
        try:
            username = self.registerUsername()
            print(username, ":username")
            print(self.request)
            print(self.client_address)
            print(self.server)
            self.chat_latest = 0
            while 1:
                msg = self.request.recv(1024)
                if(time.time() - self.chat_latest  >= 0.5):
                    self.chat_latest = time.time()
                    print(msg.decode(), "if inside")
                    if self.userman.messageHandler(username, msg.decode()) == -1:
                        self.request.close()
                        break
                else:
                    self.chat_latest = time.time()
                    print(msg.decode(), "else inside")
                    self.request.send("도배중 !".encode())

        except Exception as e:
            print(e)
        print('[%s]종료' % self.client_address[0])
        self.userman.removeUser(username)
    def registerUsername(self):
        while True:
            self.request.send('ID를 입력해주세요'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if username in user_list or username in admin:
                if self.userman.addUser(username, self.request, self.client_address):
                    return username
            else:
                self.request.send("다시 입력해주세요".encode())

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
def runServer():
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('서버종료')
        server.shutdown()
        server.server_close()
runServer()



#1. 지정 멤버만 접속 가능 IOT반 멤버
#2. 관리자이름이 따로 있다. admin
#3. 관리자 권환이 있다
    #3-1. 강제퇴장
    #3-2. 전체공지
    #3-3. 전체 채팅 비활성화
    #3-4. 퇴장 해제
#4. 유저간 귓속말 기능
    #command : /w 대상 할말
#5. 귓속말 받은 사람 출력 형태
    #보낸사람 >>> 텍스트 형태로 옴
    #ex) 하남자 >>> 난 성재민
#6. 500ms 이내에 채팅 반복 금지
#7. 비속어 필터 => 외부 파일을 통해서 필터