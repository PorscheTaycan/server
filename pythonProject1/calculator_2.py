
with open('2023_2.txt', 'r') as file:
    money = {} #빈 딕셔너리 선언
    for idx, i in enumerate(file): #파일의 모든 라인에 대한 반복
        f = i.split('\t') # 개별 라인에 대한 split으로 \t를 기준으로 리스트화
        money[idx] = f #딕셔너리의 0번키부터 위 split된 리스트를 밸류로 추가
    for i in money: #딕셔너리의 모든 키에 대한 반복
        for idx, j in enumerate(money[i]): #딕셔너리의 모든 키에 대한 밸류에 대한 반복
            money[i][idx] = money[i][idx].strip() #딕셔너리 밸류의 리스트 내부 모든 요소에 대한 공백제거
            money[i][idx] = money[i][idx].replace(',' , '') #쉼표 제거
            if '\n' in j: # \n이 나오면 split후 앞에 것만 살리는 작업
                money[i][idx] = money[i][idx].split('\n')[0]
            if money[i][idx] == '-': #하이픈을 0으로 바꾸는 작업
                money[i][idx] = "0"





def findError2(money):
    money2 = []
    for idx, i in enumerate(money):
        templist = []
        for idx2, listitem in enumerate(money[i]):
            if idx2 > 1:
                templist.append(listitem.isdigit())
            money2.append(templist)


        resultdict= {}
        for idx2, i in enumerate(money2):
            if money2[idx2].count(True)!= 11:
                if 'notTrue' not in resultdict.keys():
                    resultdict['notTrue'] = []
                resultdict['notTrue'].append(idx2+1)
        return resultdict
errordict = findError2(money)



def checkRow(dict,rowIndex):
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in dict[i]:
                if not j.isdigit():
                    print(j)



def ahapa(dict, rowIndex):
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in dict[i]:
                if not j.isdigit():
                    dict[i][searchidx] = dict[i][searchidx].replace(searchidx, '')

def ahapa2(money):
    money2 = []
    for idx, i in enumerate(money):
        templist = []
        for idx2, listitem in enumerate(money[i]):
            if idx2 > 1:
                templist.append(listitem.isdigit())
            money2.append(templist)


        resultdict= {}
        for idx2, i in enumerate(money2):
            if money2[idx2][searchidx].count(True)!= 6:
                if 'notTrue' not in resultdict.keys():
                    resultdict['notTrue'] = []
                resultdict['notTrue'].append(idx2+1)
        return resultdict



def checkNoise(dict, rowIndex):
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in range(len(money[rowIndex-1])):
                if j>1:
                    for char in dict[i][j]:
                        if not char.isdigit():
                            dict[i][j] = dict[i][j].replace(char, '')




for i in errordict:
    for j in errordict[i]:
        checkRow(money, j-1)
        checkNoise(money, j-1)
        ahapa(money, j)
        ahapa2(money)

annual_income = int(input("연봉이 얼마입니까? (원 단위로 입력하시오.)"))
tax_free = int(input("비과세액은 얼마입니까? (원 단위로 입력하시오.)"))
dependent = int(input('부양 가족수는 몇 명입니까? (본인 포함해서 작성하시요.)'))
monthly = str(int(annual_income)//12)



for searchidx, i in enumerate(money):

    if money[i][0]<= monthly < money[i][1]:

        print('근로소득세:{}'.format(int(money[searchidx][int(dependent)+1])))

