# from PIL import Image
#
# image_path = 'dd.jpg'
# image = Image.open(image_path)
# info = image.info
# print(info)
#
# info['meta'] = 'metameta'
# new_image_path = 'new_image.jpg'
# image.save(new_image_path,format='JPEG',**info)

import numpy as np
# 넘파이 : 수치 데이터 다루는 패키지
# 다차원 배열 데이터 형태를 지원
# 배열 관련 함수를 제공
# 파이썬 기본 데이터타입 리스트와 배열은 다르다.

# 넘파이 대표적인 기능
# 다차원배열로 데이터 생성 및 운용
# 배열 관련 수학, 산술 연산, 통계, 행열 처리 메서드 지원
# 브로드캐스팅 작업 가능
    # -> 크기가 다른 배열간 연산을 지원하는 기능 [0000]
    #                                      [1111] 이런 배열 원래는 [[0000][1111]] 이거니까
# 벡터화 가능
    # 스칼라  1
    # 벡터    [1
    #         2]
    # 매트릭스 [1 2
    #         3 4]
    # 텐서    [[1 2] [3 2]
    #         [1 7] [5 4]]
    # 벡터화는 반복문 사용하지 않고 배열 연산 수행을 가능하게 한다. (속도가 빠르다.)
# 파이썬 데이터 처리에 필수 패키지
# 다양한 파일형태(이미지, 텍스트, csv등..)에서 데이터 구조 추출 가능



#python 내장 데이터 타입 리스트와 numpy패키지를 통해 사용하는 배열
# 리스트와 배열은 형태가 비슷함

#파이썬 List
#각 요소에 대한 포인터를 가지고 있고, 포인터로 인해 데이터가 연속적인 메모리에 할당되는 것이
#아니기 때문에 랜덤 액세스의 시간이 오래 걸릴 수 있다.
# * 포인터 : 메모리의 주소값을 저장.
# * 랜덤엑세스(임의 접근)-> RAM : 시퀀셜 엑세스의 반대, 임의 접근
# 파이선 리스트는 다양한 데이터 타입을 가질 수 있기에, 각 요소에 대한 데이터 타입 체크 및
# 변환 과정이 내부적으로 필요하고 그에 따라 연산이 느린 편
# 파이썬의 모든 데이터는 객체 타입이다.
# 리스트는 파이썬 인터프리터에 의해 구현되어 있어 상대적으로 느린 편
# 리스트의 각 인덱스에는 객체의 실체 데이터가 아닌 요소에 할당된 객체의 주소를 가리킴
# 파이썬 리스트는 다양한 요소로 구성되어 있어 동적으로 크기가 조절된다.
# 리스트는 메모리의 레이아웃이 비순차적일 수 있다.
# 참조란 해당 객체의 메모리 주소를 가리키는 포인터를 의미



# 메모리의 영역 구분
# 1. 힙 영역
# 파이썬의 객체는 힙 영역에 할당
# 힙은 동적으로 할당되는 메모리 영역이다.
# 프로그램 실행 중에 필요한 객체즐이 저장된다.
# 리스트의 각 요소는 해당 요소가 참조하는 메모리 주소를 저장하기 때문에 실제 객체는 힙에 존재

# 2. 스택 영역
# 파이썬의 스택 영역은 호출 스택을 의미
# 호출 스택은 함수 호출과 관련된 정보를 저장
# 함수 호출 시 지역 변수, 함수의 매개변수, 반환 주소 등이 저장
# 리스트를 참조하는 변수 mylist=[]에서 mylist는 스택에 저장
# 이 변수는 실제로 힙 영역에 있는 리스트 객체를 가리키는 참조값을 포함한다.




# numpy 패키지에서 제공하는 / 타 언어에서 제공하는 배열 (ARRAY)
# 넘파이의 array 특징
# 넘파일 배열은 연속된 메모리 공간에 데이터를 저장하므로, 데이터에 대한 순차적 엑세스가 빠르다.
# 넘파이 배열은 동일한 데이터 타입으로만 구성하고, 타입 벼환, 체크가 필요 없어 빠르다.
# 넘파이 배열은 벡터화 연산을 지원하여 배열 전체 연산에 반복문 없이 가능
# 넘파이 배열의 각 요소는 실제 데이터를 담고 있음
# 넘파이 배열은 C언어 기반 저수준 언어로 구현되어 있음.
# 넘파이 배열은 각 요소가 고정된 크기를 가진다.
# 넘파이 배열은 데이터 타입에 따라 메모리에 저장되는 비트 수가 결정 됨.
# 데이터의 크기와 레이아웃이 명확함.

print([1,2,3,4])
testarr = np.array([1,2,3,4] , int )
print(testarr)
print(testarr[0])
print(type(testarr))
print(type(testarr[1]))


testarr = np.array(['1', '2', 3, 4], np.int64)
print(testarr)
print(type(testarr[1]))
print(type(testarr[2]))
# np.int64를 통해 전부 숫자 데이터 타입으로 변환되어 배열화 됨
print(testarr.dtype)
print(testarr.data)
print(testarr.shape) # (4,) 튜플형태의 벡터 형태를 반환하고, 열의 수가 4임

# 배열의 차원 개념 : dimension
# [1 2 3 4] -> 1차원 벡터 : (4,) : 4열  : 1차원 일 때에는 열이 먼저
# [1 2 3 4][5 6 7 8] -> 2차원 매트릭스 : (2,4) : 2행 4열 : 2차원 일 때에는 행이 먼저
# [1 2 3 4][5 6 7 8][9 10 11 12] -> 2차원 : (3,4) : 3행 4열

testarr = np.array([   [   [1,2,3,4],[5,6,7,8]   ], [   [9,10,11,12], [13,14,15,16]   ], [    [17,18,19,20],[21,22,23,24]   ]   ])
print(testarr)
print(testarr.shape)
# 3차원 텐서 (3, 2, 4) 형태
# 3개의 2차원 배열
# 각 2차원 배열은 2행 4열 구조
print(testarr.ndim) # ndim : N dimension : n개의 차원  -> 위의 결과 3
#ndim 프로퍼티로 몇차원인지 체크
print(testarr.size) #배열 내부 요소 수 -> 위의 결과 24

#reshape를 위한 ARR 생성
test_reshape = np.array(([1,2,3,4],[5,6,7,8]),int)
print(test_reshape)
print(test_reshape.ndim)
print(test_reshape.size)
print(test_reshape.shape)
# (2,4) 형태의 2차원 매트릭스 형태에서 8개 요소를 가지고 있는 구조를 reshape
test_reshape2 = test_reshape.reshape(8,)
print(test_reshape2)
print(test_reshape2.size)
# size가 동일한 조건 내에서 reshape로 형태 변환 가능
# (8,) 8열의 1차원 벡터로 변환

test_reshape3 = test_reshape.reshape(2,2,2)
print(test_reshape3)
print(test_reshape3.size)
print(test_reshape3.shape)
# 2 X 2 X 2 형태의 텐서로 변환

print(test_reshape3.flatten()) #평탄화 함수를 통해 n차원 배열을 1차원으로 변환
# 매트릭스, 텐서를 -> 벡터로 변환
# 총 요소 size가 같은 범위로 평탄화 됨.

# ndarray : 미지수 차원의 array
# ndarrary 인덱싱
testindex = np.array([[1,2,3],[4,5,6]], int)
print(testindex)
print(testindex[0], "1행 출력")
print(testindex[1], "2행 출력")
#리스트와 인덱싱 같은 방식 사용

#인덱스를 통한 값의 재 할당
testindex[0, 0] = 100 # 대괄호 1세트로 행, 열 인덱싱
print(testindex)
testindex[0][1] = 1500
print(testindex)
testindex[0] = 200 # 1행 인덱싱 후 값 변경시 행의 모든 열의 값이 바뀜
print(testindex)

#slice
testslice = np.array(([1,2,3,4],[5,6,7,8],[9,10,11,12]), int)
print(testslice)
print(testslice.shape)
print(testslice.size) #slice 수행을 위한 3 X 4 구조의 12size 배열 선언

print(testslice[:,:]) # 모든 것을 잘라라
print(testslice[:, :3]) # 전체 행에서 3열까지만 잘라라
print(testslice[:, :3].shape)
print(testslice[:,3].reshape(3,1))# 전체 행에서 3의 인덱스의 부분만 뜯어라 그래서 4열의 값을 가져온 것임 그런 후 reshape가 3행 1열 구조로 만들어라 : 1차원에서 2차원으로 바뀜
# 슬라이싱 + 인덱싱 혼용 가능

# 리스트의 range범위 생성 ; 배열의 arange 범위 생성
sample1 = np.arange(40)
sample2 = np.arange(0, 40, 2)
sample3 = np.arange(0, 40).reshape(4, 10)
print(sample1.shape)
print(sample2.shape)
print(sample3.shape)
print(sample3)

#np.onse 메서드
print(np.ones(shape=(10,), dtype=np.int32)) #벡터 생성

# ones메서드는 1로 채워진 배열 생성 메서드
print(np.ones((5, 2), dtype=np.int32)) # 매트릭스 생성
# 5 X 2 매트릭스
print(np.zeros(shape=(10,), dtype=np.int32))
print(np.zeros((5, 2), dtype=np.int32))
#zero 0으로 채워진 마스크 (필터)생성

print(np.empty(shape=(10,),dtype=np.int32))
#empty 메서드로 생성한 배열은 zeros와 마찬가지로 0으로 나타나지만
#차이점이 있음
# empty는 메모리에 할당이 되지 않고 형태만 선언된 상태
# zero는 메모리 할당 된 상태

# np.identity 메서드

print(np.identity(n = 5, dtype=np.int32))
#identity는 행과 열 사이즈가 같은 단위 행렬 생성
#대각 각ㅄ 1로 채워짐
print(np.eye(N=3,M=5, dtype=np.float64), "eye 3,5") # 시작위치부터 찍히게 된다.
# N : 행
# M : 열
# eye 메서드는 사선으로 1이 채워지는 배열 생성
# ndarrary의 기본 데이터 형태는 float64로 지정되고
# float형태로 생성되면 데이터에 .이 찍힌 형태로 출력 된다.

print(np.eye(3,5,k=3)) #k는 시작위치를 변경 #dtype을 따로 지정하지 않아서 float64형태
print("diag 매서드로 대각값 추출")
print(np.diag(np.eye(3,5,k=3))) # 대각 추출 시작점 = 0으로 기본값
print(np.diag(np.eye(3,5,k=3),k=3)) # 대각 추출 시작점 k = 3 으로 열 지정

#균등분포
print(np.random.uniform(0,1,10).reshape(2,5))
# uniform은 균등분포 생성
#uniform distribution
# 연속형 분포에서 일정하게 분포되는 데이터
# 균등분포란 각 결과 값을 알 수 없는 특정 이벤트의 결과 값 X가
# 예상되는 범위 a~b사이에서 균등한 확률로 일어날 것이라고 예상될 때 사용
# 위 코드는 0~1범위 균등분포 10개를 샘플링
sum = 0
arr = np.random.uniform(0, 1, 1000)
for i in range(1000):
    element = arr[i]
    sum+= element
print(sum/1000)
#1000개 샘플링 평균 출력
# 샘플링 수(표본의 수) 증가할수록 0.5수렴

# 정규분포
# noraml distribution
arr_normal = np.random.normal(0, 10, 1000)
print(arr_normal)

sum = 0
for i in range(1000):
    ele = arr_normal[i]
    sum += ele
print(sum/1000)

# 지수표기법
# e-01 / e+01 표현 : 지수 표기법
# 자리수 표기방법이다.
# 100,000의 경우 1* 10의 5제곱 -> e+05 표기

#넘파이 집계 함수 sum
arr_1 = np.arange(1,11)
print(arr_1)
print(arr_1.sum())


#axis 개념
arr_2 = np.arange(1,13).reshape(3,4)
print(arr_2)
print(arr_2.sum(axis=0)) #axis 0으로 설정 : 행방향으로의 합계
print(arr_2.sum(axis=1)) #axis 1로 설정 : 열방향으로의 합계

#(4,)의 경우 axis는 0
#(5,6) shape의 배열은 axis0은 5 axis1은 6
#3차원 텐서의 경우 axis0 : 채널 axis1 : 행 axis2 : 열을 의미 (3, 2, 4)

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a,b)))
print(np.vstack((b,a)))
#vstack 함수 : 위, 아래로 행 추가 방식의 배열 합 메서드

#hstack 함수 : 오른쪽에 열 추가 방식의 배열 합 메서드

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack((a,b)))
print(np.hstack((b,a)))

#concatenate
x = np.array([1,2,3])
print(x.ndim)
a = np.array([[1,2,3]]) # 2차원이긴 하나 데이터가 한 개 들어가 있다 예를 들어 수납을 예를 들 수 있을 듯
print(a.ndim)
b = np.array([[4,5,6]])
print(b)
print(np.concatenate((a,b),axis=0)) # 행방향
print(np.concatenate((a,b),axis=1)) # 열방향
#concatenate 함수는 axis 옵션 매개변수를 통해 방향을 설정



a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])
print(b)
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b.T),axis=1)) # .T라는 것은 돌려주는 것이다. 원래는 12   56 이 형태 인데 맞질 않아서 56을 돌려줘서 125
                                            #                                34                                       346 이렇게 된 것이다.
# .T로 변형
# 혹은 .transpose() 메서드로 변형

# Array간 연산
oper_arr = np.array([1,2,3])
print(oper_arr)
print(oper_arr*oper_arr)


# 같은 형태의 배열끼리 사칙연산은 같은 자리 수끼리 연산 됨

broad_arr = np.array([[1,2,3],[4,5,6]])
print(broad_arr) # 2차원 매트릭스 생성
x = 10
print(broad_arr + x)
print(broad_arr * x)
print(broad_arr - x)
print(broad_arr // x)
# 브로드 캐스팅은 형태가 다른 배열 or 스칼라와 연산 지원

# 매트릭스와 베터와 브로드캐스팅
broad_matrix = np.arange(1,13).reshape(4,3)
print(broad_matrix) # 4 X 3 구조 매트릭스 생성
broad_vector = np.arange(10, 40,10)
print(broad_vector)
print(broad_matrix + broad_vector) # 2차원 매트릭스 + 1차원 벡터


#Comparison 넘파이 배열간 비교 연산
comp = np.arange(10)
print(comp)
print(comp>5) # 모든 요소에 비교 연산 > 5에 대한 T/F값이 리턴되는데 벡터
print(np.all(comp>5))
# np.all은 모두 만족하면 True 그렇지 않으면 False
# np.any()는 하나라도 만족하면 True 하나도 만족 못하면 False
print(np.any(comp>5)) #comp 벡터에 5이상의 값이 하나라도 있기 때문에 True

# all and 연산자
# any or 연산자



where_arr = np.arange(10)
print(where_arr)
print(np.where(where_arr>5,1,0))
# 조건식 > 5가 참일 경우 치환을 1로 하고 거짓일 경우 0으로 치환하는 where함수


#데이터의 전처리
    #노이즈 검사
    #결측지 검사 np.nan
#데이터의 정제

def nans(shape, dtype = np.float64):
    a = np.empty(shape,dtype)
    a.fill(np.nan) # 값을 채우는 fill 함수 np.nan 값으로
    #nan : not a number의 의미
    #nan은 결측값 missing value 혹은 유효하지않음을 나타낼 때 사용
    # float 타입
    #numpy에서 사용되는 특수한 값
    return a
print(nans([3,4]))
nan_arr = np.array([1,2,3,np.nan,5])
print(np.isnan(nan_arr)) #nan값을 검사하는 메서드 isnan
print(np.isnan(nans([3,4])))

arg_arr = np.array([[1,2,3,40,50,60,7,8,9],[10,11,12,13,14,15,16,17,18]])
print(arg_arr)
print(np.argmax(arg_arr,axis=0)) # axis = 0은 행을 의미하고 행에서 최대값을 가진 위치를 반환
print(np.argmax(arg_arr,axis=1)) # argmax는 최대값 위치 반환 axis = 1은 열 기준

