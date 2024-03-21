#python gui

import tkinter # GUI 모듈 포함
root = tkinter.Tk() # main프레임



root.title(" GUI 프로그램 ") # 프로그램 명
root.geometry("1600x800+100+100") #1600 800 사이즈를 100 +100 시작위치로 정하는 것임 # 해상도, 시작위치
root.resizable(False, False) # 사이즈 조정 못함 # 사이즈 조절 가능 여부 설정

label = tkinter.Label(root, text="sample") # root에 올린다.
label.pack() # pack은 여분 공간을 기준으로 밑에 생성된다.
label2 = tkinter.Label(root, text="sample2", width=10 , height=10 , fg="red") # label 사이즈가 10, 10이라서 바로 붙는 것이 아니다. 그리고 글씨색 빨간색으로 설정
label2.pack()

#################
# label 컨트롤 매게변수
# text : 라벨에 들어갈 문자열
# textvariable : 라벨에 표시할 문자열을 가져올 변수명
# justify : 라벨의 문자열이 여러줄일 때 정렬 [center/left/right]

# width : 라벨 너비
# height : 라벨 높이
# relief : 라벨 테두리 모양 [ flat / groove / solid ] -> border을 뜻함.
# borderwidth : 테두리 두께 [숫자]
# fg : 글씨색 [색상명]
# bg : 배경색 [색상명]
# padx : x축 패딩 [숫자]
# pady : y축 패딩 [숫자]
# state : 라벨의 상태 [normal / active / disabled]
# highlightcolor : 라벨 선택되었을 때 색상 [색상명]
# cursor : 라벨에 나타나게 할 커서의 종류 [커서속성명]
# 커서 속성명 종류 [arrow / cross / dot 등]

count = 0
def xxxx():
    global count # 전역변수 count를 함수내에서 사용
    count+= 1 # count 값 1 늘리기
    label.config(text=str(count)) # config를 통해 라벨의 텍스트를 count숫자를 str로 변경한 값으로 주겠다.

button = tkinter.Button(root, overrelief='solid', width=15, command=xxxx,  # command = 함수명, 호출아님 이 형태 # command 버튼에 함수 연결 속성
                        repeatdelay=1000, # 반복을 1초간 누르면 시작
                        repeatinterval=100)  #0.1초 주기로 반복
button.pack()

# button.invoke() 버튼을 실행
# button.flash() 버튼 깜빡임
# 버튼에 사용가능한 속성
# text 버튼에 표시할 텍스트
# textvariable 버튼에 표시할 문자열을 가져올 변수명 설정
# anchor 버튼 내 텍스트의 위치 설정 [center/n/w/s/e] 중아, 동서남북
# justufy 버튼 문자열이 여러 줄 일 때 정렬 방법 [center/left/right]
# width
# height
# bg
# fg
# padx, pady
# state
# highlightcolor : 버튼이 선택되었을 때의 색상 [색상명] -> button.flash() 가 있어야 실행됨
# highlightbackground : 버튼이 선택되지 않았을 때의 색상 [색상명] -> button.flash() 가 있어야 실행됨
# command : 함수 연결, 함수명을 쓴다.
# repeatdelay : 반복 시작 대기 시간 [ms]
# repeatinterval : 반복 눌림 주기 [ms]

def xx(e): # e 넣는 이유 키보드를 전달받을 수 있는 이벤트의 매개변수가 있어야한다.
    label2.config(text=str(eval(entry.get()))) #eval 수식을 계산해서
entry = tkinter.Entry(root)
entry.bind("<Return>", xx) #xx에는 함수명이 들어간다.
entry.pack()

# entry에 사용하는 메서드 목록
# insert(index, 문자열) : index위치에 문자열 추가
# delete(idx1, idx2) : idx1부터 idx2까지 문자열 삭제
# get : 엔트리의 텍스트 가져오기
# index(idx) : idx대응 위치 획득
# icursor(idx) : idx앞 키보드 커서 설정
# select_to(idx) : 키보드 커서부터 idx까지 블록처리
# select_clear() : 블록처리 해제

# entry 컨트롤에 적용가능한 속성 목록
# justify
# textvariable
# width
# bg
# fg
# insertwidth : 입력창의 커서 너비 [숫자]
# insertbackground : 입력창의 커서 색상 [색상명]
# selectForeground : 문자열 블록처리 부분의 글씨 색상 [색상명]
# selectbackground : 문자열 블록처리 부분의 배경 색상 [색상명]
# state : 입력창의 상태 설정 [normal / readonly / disabled]
# disabledbackground : disabled 상태에서의 배경 색 [색상명]
# disabledforeground : disabled 상태에서의 글 색 [색상명]

listbox = tkinter.Listbox(root, selectmode="extended", height=0)
# selectmode = extend : 다중 선택 가능 , 시프트 누른채로 방향키로 멀티 셀렉션 가능
# selectmode = single : 단일 선택만 가능
listbox.insert(0, "김지욱") # 리스트박스에 항목 추가
listbox.insert(1, "성재민")
listbox.insert(2, "진정현")
listbox.insert(3, "강병헌")
listbox.delete(1,2) # 1부터 2까지 항목 삭제
listbox.pack() # 리스트 박스 배치

# listbox 메서드
# insert(idx) : idx위치에 항목 추가
# delete(a, b) : a에서 b위치까지 항목 삭제
# ativate(idx) : idx위치의 항복을 선택 (활성화)
# curselection() : 선택한 항복을 튜플로 묶어서 반환해주는 함수
# get(a, b) : a부터 b위치까지 항목을 튜플로 반환
# index(idx) : idx위치 값 획득
# see(idx) : idx가 보이는 위치로 조정

# listbox 속성
# listvariable : 리스트 박스에 표시할 문자열 가져올 변수명
# width
# height
# releif
# bg
# fg
# selectbackground : 블록처리 배경 색상 [색상명]
# selectforeground : 블록처리 문자 색상 [색상명]
# selectborderwidth : 블록처리 테두리 두께 [숫자]
# cursor
# state
# selectmode : 선택 모드 [single / multiple / extended]


checkVariety_1 = tkinter.IntVar() # tkinter안에 있는 인수형태의 변수 만들 때 이렇게 만들어야함.
checkVariety_2 = tkinter.IntVar()

def f():
    checkbutton.flash()


checkbutton = tkinter.Checkbutton(root, text="1", variable=checkVariety_1, activebackground='red')
checkbutton2 = tkinter.Checkbutton(root, text="2", variable=checkVariety_2)
checkbutton3 = tkinter.Checkbutton(root, text="3", variable=checkVariety_2, command=f)
#여러개 체크박스는 변수(속성)를 통해 묶는다.

checkbutton.pack()
checkbutton2.pack()
checkbutton3.pack()

# 체크박스 메서드
# select() 체크상태
# deselect() 체크해제
# invoke() 체크버튼 실행
# flash() 깜빡임

# 체크박스 속성
# text 체크박스 문자열
# textvariable 체크버튼에 표시할 문자열 가져올 변수명
# anchor
# justify
# width
# height
# relief
# fg
# bg
# padx
# pady
# cursor
# state
# activebackground
# activeforeground
# disabledforeground
# commad : 함수 연결
# variable : 체크버튼 상태 저장할 제어 변수 [tkinter.IntVar()]


# 라디오 버튼
RadioVariety_1 = tkinter.IntVar()
RadioVariety_2 = tkinter.IntVar()

def X():
    label.config(text=str(RadioVariety_1.get()))
    label2.config(text=str(RadioVariety_2.get()))
    radio4.deselect()

radio1 = tkinter.Radiobutton(root, text="111", value=100, variable=RadioVariety_1, command=X)
radio2 = tkinter.Radiobutton(root, text="222", value=200, variable=RadioVariety_1, command=X)
radio3 = tkinter.Radiobutton(root, text="333", value=300, variable=RadioVariety_1, command=X)
radio4 = tkinter.Radiobutton(root, text="444", value=400, variable=RadioVariety_2, command=X)

#radio1~3이 RadioVariety_1에 묶인 1번 그룹
#radio4가 RadioVariety_2에 묶인 2번 그룹

radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()


# 라디오버튼 메서드
# select() 체크 상태
# deselect() 해제 상태
# invoke()
# falsh()


# 라디오버튼 속성
# text
# textvariable
# anchor
# width
# height
# padx, pady
# command
# value 라디오버튼이 가진 값 설정
# variable 라디오버튼 상태를 저장하려는 변수 지정 속성





# 컨트롤 배치 방법 1. pack 2. place 3. grid
# 1. pack 방식으로 배치할 때 속성
# side 속성에 배치 방향 설정 [left right top bottom]
# pack은 grid배치 방법과 혼용 불가능 place 배치와 혼용 가능
# anchor
# expand 미사용 공간 확보 속성 [boolean지정 -> True or False] 키다 끄다로 설정
# padx
# pady
# fill 할당 공간에 대한 크기 설정 [none/x/y/both]

#root.mainloop()

# 2. place 방식으로 배치시 속성
root2 = tkinter.Tk()  # 새로운 폼 만들기
root2.geometry("600x600")
root2.title("root2")
b1 = tkinter.Button(root2, text="좌표설정 300_1")
b1.place(x=300, y=1) # 좌표임
b2 = tkinter.Button(root2, text="200 200")
b2.place(x=200, y=200)
b3 = tkinter.Button(root2, text="pack btn")
b3.pack()

#root2.mainloop()


#3. grid 방식 배치
# 그리드 방식의 배치는 레이아웃을 셀단위로 나누고 셀 위치를 통해 배치하는 방법
root3 = tkinter.Tk()
root3.geometry("600x600")
root3.title("root3")
root3.resizable(1,1)

b11 = tkinter.Button(root3,text="0 0")
b22 = tkinter.Button(root3, text="0 1", width=100)
b33 = tkinter.Button(root3, text="0 2")

b44 = tkinter.Button(root3,text="1 0")
b55 = tkinter.Button(root3, text="1 1")
b66 = tkinter.Button(root3, text="1 3")

b11.grid(row=0, column=0)
b22.grid(row=0, column=1)
b33.grid(row=0, column=2)
b44.grid(row=1, column=0, rowspan= 2)
b55.grid(row=1, column=1, columnspan = 3)
b66.grid(row=1, column=3)


root3.mainloop()


