import threading # 인력이 두개?
import time
count = 0
def sum(low, high):
    total = 0
    count = 0
    for i in range(low, high):
        total+=i
    print("subthread", total)
    while 1:
        count+=1
        time.sleep(5) # 5초마다 센서값 갱신
        print("\nsubthread 실행", count)

def sum2(low, high):
    print("sum2 thread")

x = threading.Thread(target=sum, args=(1, 1000)) # 서브 스레드  # ex) 왼손
x.start()
listx = []

def hello():
    print("hello")
while 1:
    if input("mainThread input prompt"): # 메인 스레드 # ex) 오른손
        hello()
    time.sleep(0.2)