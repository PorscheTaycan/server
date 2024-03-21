import random
import tkinter
def select_rand_color():
    colors = ["red", "yellow", "blue"] # 색상 리스트
    rand_color= random.choice(colors) # 랜덤으로 임의 색상 1개 추출
    listbox.insert(tkinter.END, rand_color) #항목추가
    listbox.itemconfig(tkinter.END,{'fg': rand_color})
    #item에 대한 fg색 config수행

def get_selection(event):
    global stringv
    index = listbox.curselection()[0] # 튜플로 리턴 오기때문에 인덱싱0번
    print(index)
    value = listbox.get(index)
    print("선택 리스트 항목의 값 -> ", value)
    stringv.set("/w "+value+" ")
    entry.icursor(len(entry.get()))
    root.after(1,entry.focus_set) # after는 1이라는 지연시간

root = tkinter.Tk()
root.geometry("300x300")
listbox = tkinter.Listbox(root)
listbox.pack()
stringv = tkinter.StringVar()
entry = tkinter.Entry(root,textvariable=stringv)
entry.pack()
btn = tkinter.Button(root, command=select_rand_color, text = "항목추가")
btn2 = tkinter.Button(root, command=root.destroy, text="종료")
listbox.bind("<<ListboxSelect>>", get_selection)
btn2.pack()
btn.pack()
root.mainloop()