# bg={"bg1":4000,"bg2":3500,"bg3":5000,"bg4":3300,"bg5":3700}
# dr={"dr1":1500,"dr2":1500,"dr3":1500}
# ds={"ds1":1800}

side={"f":0,"f+c":1500,"c":500}

prices=[0,2000,500]
bsk={}
selected_cat="rec"
cat_selected=False
def addToBsk(item,amount=1,L=False,S=False,Sitems=""):
    if L==True:
        item=item+"L"
    if S==True:
        item=item+"S_"+Sitems
    if item not in bsk:
        bsk[item] = 0
    bsk[item] += amount
def setAmount():
    amount_value = 1
    while True:
        amount = input("1.수량+ 2.수량- 그 외 입력:다음 단계")
        if amount == "1":
            amount_value += 1
        elif amount == '2':
            if amount_value > 1:
                amount_value -= 1
            else:
                print("1개 이하 설정 불가")
        else:
            return amount_value

while True:
    bg = {}
    dr = {}
    ds = {}
    menulist = [bg, dr, ds]
    with open("menu.txt", "r") as file:
        for idx, i in enumerate(file):
            temp = i.split(',')
        #temp = file.readline().split(',')
            for j in temp:
                if '\n' in j:
                    j = j.replace('\n', "")
                if not j.isdigit():
                    menulist[idx][j] = 0
                else:
                    menulist[idx][list(menulist[idx].keys())[-1]] = j

    rec = {list(bg.keys())[0]: list(bg.values())[0], list(bg.keys())[1]: list(bg.values())[1]}
    category={"rec": rec, "burger": bg, "drink": dr, "dessert": ds}
    place=input("1.포장 2.매장")
    while True:
        cat_selected = False
        print("*" * 20)
        for i in range(len(list(category.keys()))):
            print(i+1,list(category.keys())[i])
        for i in range(len(category[selected_cat].keys())):
            print(i+len(category.keys())+1,list(category[selected_cat].keys())[i])
        userCh=input("번호입력")
        for i in range(len(category.keys())):
            if int(userCh)==i+1:#카테고리를 선택한 경우의 코드 부분
                selected_cat = list(category.keys())[int(userCh)-1]
                cat_selected=True
                break
        if cat_selected==False:
            if int(userCh)-1-len(category) < len(category[selected_cat]):
                print(list(category[selected_cat].keys())[int(userCh)-1-len(category)])
                if selected_cat in category:
                    sel_m_num=int(userCh) - len(category)
                    if  list(category[selected_cat].keys())[sel_m_num-1] in bg:
                        while True:
                            set_size=input("1.일반세트 2.라지세트 3.단품")
                            if  set_size!="1" and set_size!="2" and set_size!="3":
                                continue
                            if set_size=="3":
                                amount_value = setAmount()
                                addToBsk(list(category[selected_cat].keys())[sel_m_num-1],amount_value)
                                break
                            else:
                                for i in range(len(side)):
                                    print("{}.{}".format(i+1,list(side.keys())[i]))
                                sel_s_num=input()
                                for i in range(len(dr)):
                                    print("{}.{}".format(i + 1, list(dr.keys())[i]))
                                sel_d_num=input()
                                print(list(category[selected_cat].keys())[sel_m_num-1],list(side.keys())[int(sel_s_num)-1],list(dr.keys())[int(sel_d_num)-1])
                                confirm=input("1.확인 2.취소")
                                if confirm!="1":
                                    break
                                amount_value=setAmount()
                                if set_size=="2":
                                    addToBsk(list(category[selected_cat].keys())[sel_m_num-1],amount_value,L=True,S=True,Sitems=(list(category[selected_cat].keys())[sel_m_num-1]+list(side.keys())[int(sel_s_num)-1]+list(dr.keys())[int(sel_d_num)-1]))
                                else:
                                    addToBsk(list(category[selected_cat].keys())[sel_m_num-1],amount_value, L=False,S=True, Sitems=(list(category[selected_cat].keys())[sel_m_num - 1] +list(side.keys())[int(sel_s_num) - 1] + list(dr.keys())[int(sel_d_num) - 1]))
                                break
                    else:
                        amount_value=setAmount()
                        addToBsk(list(category[selected_cat].keys())[int(userCh)-1-len(category)],int(amount_value))
                    mode=1
                    while mode:
                        print(bsk)
                        mode=input("1.수량변경 2.품목삭제 3.추가주문 4.결제")
                        if mode=="3":
                            break
                        elif mode=="4":
                            break
                        elif mode=="1":
                            target_idx=input("수량변경하려는 품목의 번호입력 1부터")
                            amount_value=input("수량변경하려는 품목의 수량 입력 숫자")
                            bsk[list(bsk.keys())[int(target_idx)-1]]=int(amount_value)
                            continue
                        elif mode=="2":
                            target_idx = input("수량변경하려는 품목의 번호입력 1부터")
                            del bsk[list(bsk.keys())[int(target_idx)-1]]
                            continue
                    if mode=="4":
                        print("결제완료 후 첫화면 진입")
                        break