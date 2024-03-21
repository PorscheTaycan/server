import tkinter
class ButtonApp: # 동적 생성 해서 만드는 것
    def __init__(self, master):
        self.master = master # master를 전달받아서 form을 만들고 있다.
        self.master.title("button click APP")
        self.label_var = tkinter.StringVar()
        self.label = tkinter.Label(self.master, textvariable=self.label_var)
        self.label.pack(pady=20)

        for i in range(1, 11):
            button = tkinter.Button(self.master, text = f"Button{i}", command=lambda button_number=i: self.update_label(button_number))
            #lambda 식의 구성은 lambda 매개변수 : 실행코드 형태이다.
            #lambda에 button_number 매개변수 명을 통해 for의 i값을 지정
            #update_label함수의 매개변수 button_number 매개변수로 전달 됨.
            button.pack(pady = 5)

    def update_label(self, button_number):
        self.label_var.set(f"Button{button_number} clicked")

root = tkinter.Tk() # form 객체 생성 과정
app = ButtonApp(root) # ButtonApp 클래스로 만든 인스턴스 생성자에 root폼을 매개변수로 전달
app.master.mainloop() # app인스턴스의 self.master인 root폼으 실행시킴
