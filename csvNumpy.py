import tkinter as tk
from tkinter import filedialog
import pandas as pd
from io import StringIO


class CSVeditor:
    def __init__(self, master):
        self.master=master
        self.master.title("테스트")
        self.load_button = tk.Button(self.master, text="csv로드", command=self.load_csv)
        self.load_button.pack(pady = 10)

        self.text_box = tk.Text(self.master, height=10, width=50)
        self.text_box.pack(pady=10)

        self.save_button = tk.Button(self.master, text="저장", command=self.save_change)
        self.save_button.pack(pady=10)

    def load_csv(self):
        file_path=filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        #filedialog.askopenfilename()
        #filedialog에서 제공하는 파일 대화상자를 통한 파일 선택 메서드
        if file_path:
            try:
                self.df = pd.read_csv(file_path, encoding='cp949') # 인코딩방식 1
                print(type(self.df))
            except:
                self.df = pd.read_csv(file_path, encoding='utf-8') # 인코딩 방식 1
            #cp949인코딩에서 오류나면 utf-8로 열도록 에외처리
            self.text_box.delete(0.0,tk.END)
            self.text_box.insert(tk.END, self.df.to_string(index=False))
            # df는 데이터프레임이라는 판다스에서 제공하는 데이터 형태이고 엑셀, csv같은 테이블 구조
            # 데이터 프레임은 0부터 인덱스를 가진다.
            # to_string메서드는 데이터프레임을 문자열로 반환

    def save_change(self):
        if hasattr(self, 'df'): # hasattr 속성을 가지고 있냐를 체크하는 함수
            edited_data = self.text_box.get('0.0', tk.END)
            edited_df = pd.read_csv(StringIO(edited_data))
            file_path = filedialog.askopenfilename(defaultextension='.csv',filetypes=[("CSV Files", "*.csv")])
            if file_path:
                edited_df.to_csv(file_path,index=False)
                tk.messagebox.showinfo("success", "변경 완료")

root = tk.Tk()
csv_editor=CSVeditor(root)
csv_editor.master.mainloop()