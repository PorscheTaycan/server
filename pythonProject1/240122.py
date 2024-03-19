#240122

#클래스 사용 이점
#class
#모듈화
#생성자  __init__
#추상화
#함수를 포함한다.
#클래스는 식별자
#소멸자  __del__
#필드
#self
#틀
#객체
#object
#인스턴스

class testclass: #클래스 명 (틀)
    def __init__(self): #생성자(메서드): 객체생성시 호출
        self.name='testclass' #필드
    def __del__(self): #소멸자(메서드)
        pass

testclass1=testclass() #틀로 객체 생성
print(testclass1.name) #객체 출력

#testclass1은 객체이다
#testclass1은 testclass 클래스로 만든 객체이다
#testclass1은 object이다
#testclass1은 testcllass의 인스턴스이다.


#클래스 구조를 이용해서
#4개의 계산기가 돌아갈 수 있게 구현
#두 개의 숫자만 연산
#사칙연산만 지원
#실행 코드 x, 계산기 4개에 대한 객체 생성만
#작성 후 드라이브 업로드 240122_01.py
class Calculator:
    def __init__(self):
        self.result = 0

    def plus(self,num):
        self.result += num
        return self.result

    def minus(self,num):
        self.result -= num
        return self.result

    def multiplication(self,num):
        self.result *= num
        return self.result

    def division(self,num):
        self.result /= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()
cal4 = Calculator()



#강사님
class Cal:  #계산기 생성
    value = 200 # 클래스 변수
    ssss = 200
    def __init__(self):
        self.name = "계산기" # 필드 : 객체마다의 독립적 변수 인스턴스 변수
        self.num1 = 0
        self.num2 = 0
        self.value = 0
    def sum(self, x, y):
        self.num1 = x
        self.num2 = y
        self.value = self.num1 + self.num2
        return self.num1 + self.num2
    def sub(self, x, y):
        self.num1 = x
        self.num2 = y
        self.value = self.num1 - self.num2
        return self.num1 - self.num2
    def mul(self, x, y):
        self.num1 = x
        self.num2 = y
        self.value = self.num1 * self.num2
        return self.num1 * self.num2
    def div(self, x, y):
        self.num1 = x
        self.num2 = y
        self.value = self.num1 / self.num2
        return self.num1 / self.num2

    def __del__(self):
        print("{}-파괴되었습니다.".format(self.name))

    def quit(self):
        self.__del__()




num1 = Cal()  #계산기를 실행했다.
num2 = Cal()
num3 = Cal()
num4 = Cal()

#각 4개의 계산기는 독립적인 인스턴스
print(num2.value) #객체 기준으로 접근 value변수 : 인스턴스
print(num2.ssss)
print(Cal.value) #클래스로 접근

# 클래스 변수 : 특정 클래스로 만들어진 객체끼리 공유하는 데이터
# 인스턴스 변수 : 만들어진 인스턴스 객체 전용 데이터


class fortest:
    def __init__(self):
        self.x = 0
    def __enter__(self):  #진입
        return self #self: 인스턴스 객체 지향   #return self 가 as test에 넣어주는 식별자 역할
    def __exit__(self, exc_type, exc_val, exc_tb):  #예외처리 관련  #나온다
        #예외 발생하지 않으면 모두 None 상태   #self.close()가 있다
        pass

with fortest() as test:  #식별자가 test
    print(test)

class human:
    def __init__(self):
        pass
print(human())
human1 = human()  #식별자는 human1
print(human1)


#클래스 변수 :
# 1. 클래스에 속한 변수
# 2. 클래스의 모든 인스턴스 간 공유 가능
# 3. 클래스 정의 내부에서 생성
# 4. 클래스 자체 속성 상태

#인스턴스 변수 :
# 1. 각 인스턴스에 속한 변수로 인스턴스와 연결되어 있음
# 2. 독립적인 변수
# 3. 객체 자체의 속성 상태 등 표현

class myclass:
    instlist=[]
    count = 0
    grp = 1
    def __init__(self):
        myclass.count+=1
        myclass.instlist.append(self)
        self.name="dddd"
    def __del__(self): #수동 호출 X -> 파이썬 메모리 문제 생길 가능성
        print("삭제", self)
        myclass.count-=1
class1=myclass()
class2=myclass()
class3=myclass()

del class2 #del 키워드로 객체 삭제
print(myclass.count)
print(myclass.grp)


class ttt: #init 함수가 없다.
    def setdata(self, a):
        self.a=a
t = ttt() #생성자 함수가 없어도 객체 생성 가능
#생성자 함수를 쓰는 이유 : 자동호출
print(t.a)
t.setdata(("dddd"))
print(t.a)


class c1:#차등을 주거나 큰 클래스 가져오거나 변형되게 만들 때 상속을 해준다.
    def __init__(self, name):
        self.name=name
    def show(self):
        print(self)
    def plus(self, a, b):
        return a+b
#클래스의 상속 inherit


class c2(c1): #클래스명(상속받을 클래스명)
    #c2가 c1을 상속받아 모든걸 물려받게 된다.
    def m(self, a, b):
        return a-b
    def show(self):
        return self #self -> 인스턴스 객체 자기 자신을 의미

ins2 = c2("c1으로부터 상속받은 c2클래스의 인스턴스")
print(ins2.name)
print(ins2.show())
# ins3 = c2()
#메서드 오버라이딩

if isinstance(ins2, c1):
    print("True")

class c3(c1):
    def c3method(self):
        print("c3에만 구현된 함수")

class c4(c2, c3):
    def c4method(self):
        self.c4Value = 100
        self.__c4V = 100 # __ 프라이빗 함수 ( 클래스 밖에서 사용 불가)
        #게터와 세터를 통한 사용을 해야한다.

        print("c2+c3")
    def showc4V(self):
        print(self.__c4V)
    def setc4V(self,value):
        self.__c4V = value

cc4 = c4("123")
cc4.c4method()
print(cc4.c4Value)
cc4.showc4V()  #getter 조회
cc4.setc4V(500)
cc4.showc4V()  #setter 제공



# 추상화
# 클래스 구조로
# 콘솔에서 진행되는
# 1. 건물 2. 사람 3. npc 4. 맵 5. 운영
#