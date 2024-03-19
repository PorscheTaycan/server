import time
from bomb import Bomb
import random
# from item import Item
tick=0
class Map:
    def __init__(self, size=15): #size= 15 범위설정
        self.size = size
        self.map = self.create_map() #맵만드는 함수 구현
        self.map[1][1] = 2
        self.map[13][13] = 3
    def set_user_position(self,x,y):
        # if Item.shield_value==0:
        #     self.map[x][y] = 2
        # else:
        #     self.map[x][y] = 12
        self.map[y][x] = 2
    def set_ai_position(self,x,y):
        self.map[y][x] = 3
    def del_user(self,x = 1,y = 1):
        if self.map[y][x] != 11:
            del self.map[y][x]
            self.map[y].insert(x, "*")
    def create_map(self): #맵만들기
        # 맵 초기화
        game_map = [] #빈리스트 만들기

        for i in range(self.size):#15 행
            row = [] #행
            for j in range(self.size): #15 열
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1: #i가 0이거나 14이거나 j가 0이거나 j=14이거나
                    row.append(0)  # 외벽
                elif i % 2 == 0 and j % 2 == 0:
                    row.append(1)  # 고정 벽
                else:
                    row.append('-')  # 빈 공간
            game_map.append(row)
        return game_map

    def set_bomb_position(self, x, y):
        self.map[y][x] = 11

    def break_wall(self): #아이템이 나오는 벽 만들기
        for i in range(1,self.size-1): #외곽 제외
            for j in range(1,self.size-1): #외곽 제외
                if self.map[i][j]=='-': #빈칸이라면?
                    if not (i<=3 and j<=3) or (i>=11 and j>=11) : #처음 위치에서 제외범위 만들기
                        if (i % 3 == 0 and j % 3 ==0)or(i % 3 == 1 and j % 3 ==1): #규칙성 식
                            self.map[i][j]=4 #좌표에 4찍기
    def remove_wall_in_bomb_range(self, bomb):
        sorted_ranges = bomb.bomb_range() #이중리스트
        if bomb.ticks==bomb.original_ticks+4:
            self.map[bomb.x][bomb.y] = "+"
            for direction_range in sorted_ranges:  # 상, 하, 좌, 우 방향별로 순회 밑에서 브레이크만나면 다음방향으로
                for x, y in direction_range: #상방향이면 거기안 원소들 x,y로 출력
                    if 0 <= x < self.size and 0 <= y < self.size:
                        # 장애물에 따라 처리
                        if self.map[x][y] in [0, 1]:
                            break  # 해당 방향으로의 폭발 중단 아무일도 안벌어지게하는거임
                        elif self.map[x][y] == 4:
                            ran_list = ['-', 5, 6, 7, 8]
                            probabilities = [0.2,0.2, 0.2, 0.2, 0.2]  # 각 아이템의 확률
                            # 무작위로 아이템 선택
                            selected = random.choices(ran_list, weights=probabilities)[0]
                            self.map[x][y] = selected  # 아이템 벽은 공백으로 제거
                            break
                        else:
                            self.map[x][y] = 9  # 폭발 범위 표시
    def clear_explosion(self,bomb):
        if bomb.ticks == bomb.original_ticks + 5: #5틱지났으면 범위 삭제
            for i in range(self.size):
                for j in range(self.size):
                    if self.map[i][j] in [9, '+']:  # 폭발 범위 또는 폭탄 위치
                        self.map[i][j] = '-'
    def display_map(self): #사이사이 띄어쓰기넣어서 출력
        for row in self.map:
            row_string = ''
            for cell in row:
                row_string += str(cell) + ' '
            print(row_string)
    def end_map(self): #$를 맞으면 죽는벽으로 구현하기, 틱 50이상일때 시작하는걸로 우선 나중에 수정
        a = 1
        b = self.size - 1
        while a<b:
            for i in range(a,b):
                self.map[a][i]='$'
                self.display_map()

            for i in range(a+1,b):
                self.map[i][b-1]='$'
                self.display_map()

            for i in range(b-2,a-1,-1):
                self.map[b-1][i]='$'
                self.display_map()

            for i in range(b - 2, a - 1, -1):
                self.map[i][a] = '$'
                self.display_map()
            a += 1
            b -= 1
    def item_coordinate(self):
        item_coor={}
        for i in range(1, self.size - 1):  # 외곽 제외
            for j in range(1, self.size - 1):  # 외곽 제외
                if self.map[i][j] in [5,6,7,8]:
                    item_type=self.map[i][j]
                    item_coor[item_type]=i,j
        return item_coor


    def get(self):
        return self.map


# 맵 생성 및 표시
game_map = Map()
game_map.break_wall()
bomb_instance = Bomb(7, 9, "some_info", 17)
bomb_instance.tick(21)
game_map.remove_wall_in_bomb_range(bomb_instance)
game_map.display_map()
bomb_instance.tick(22)
game_map.clear_explosion(bomb_instance)
game_map.display_map()
bomb_instance.tick(23)
game_map.display_map()
bomb_instance.tick(24)
game_map.display_map()
bomb_instance.tick(25)
game_map.display_map()

# game_map.end_map()
class Itemlist:
    user_items = [5,5,6,7,8]                                # 임의의 유저 아이템 리스트
    bomb_list = [1]                                         # 폭탄의 default
    a = {"5":"a","6":"b","7":"c","8":"d"}                   # 아이템의 값이 들어있는 리스트

    life = 1  # 우선 라이프로 표현한건데, hp 체력으로 처리해도 될 듯. 데미지 무효,무적 되게 (폭탄 데미지 +1) 이런식의 체력 줘도 될 듯.
    b_range = user_items.count(5)
    b_count = user_items.count(6)
    shield_value = user_items.count(7)
    # 아이템

    def __init__(self):
        # 해당 클래스의 초기화 메서드에서 인스턴스 변수를 초기화하도록 변경
        self.user_items = []
        self.bomb_list = []
        self.a = {}
        self.life = 1
        self.b_range = 0
        self.b_count = 0
        self.shield_value = 0

    def itemlist(self, value):
        if value == "5":  # 아이템 번호가 5번일 경우 리스트에 5 들어가기
            Itemlist.user_items.append(5)
            self.b_range += 1
            return self.b_range
        elif value == "6":  # 아이템 번호가 6번일 경우 리스트에 6 들어가기
            Itemlist.user_items.append(6)
            self.b_count += 1
            print("폭탄 개수 증가")  # 중첩 가능
            return self.b_count
        elif value in ["7", "8"]:
            if int(value) not in Itemlist.user_items:
                # "7" 또는 "8"이 없을 때 실행할 코드
                if value == "7":  # 아이템 번호가 7번일 경우 리스트에 7 들어가기
                    Itemlist.user_items.append(7)
                    print("방어")  # 중첩 불가능
                elif value == "8":  # 아이템 번호가 8번일 경우 리스트에 8 들어가기
                    Itemlist.user_items.append(8)
                    print("던지기")  # 중첩 불가능
class Bomb:

    def __init__(self, x, y, user_imf, ticks):
        self.x = x
        self.y = y
        self.user_imf = user_imf
        self.ticks = ticks
        self.b_range_v = 3
        self.b_count = 3

    def tick(self):
        self.ticks += 1
        return self.ticks

    def bomb_count(self):
        self.b_count -= 1
        return self.b_count

    def bomb_range(self):
        x_left = self.x - self.b_range_v
        x_right = self.x + self.b_range_v
        y_up = self.y + self.b_range_v
        y_down = self.y - self.b_range_v
        return x_left, x_right, y_up, y_down



class User:
    user_items = []

    def __init__(self):  # 시작 좌표 (1, 1)
        self.x = 1
        self.y = 1
        self.has_bomb = False
        self.is_die = False
        self.life_count = 3
        self.items = []
        self.shield_value = self.user_items.count(7)
        self.b_count = self.user_items.count(6)





    def move_x(self, direction):
        if direction == 4:
            self.x -= 1  # 왼쪽으로 이동
        elif direction == 6:
            self.x += 1  # 오른쪽으로 이동
        return self.x
    def move_y(self, direction):
        if direction == 2:
            self.y -= 1  # 아래쪽으로 이동
        elif direction == 8:
            self.y += 1  # 위쪽으로 이동
        return self.y

    def bomb(self, direction):
        if direction == 5: # 5번 누를 시 폭탄 설치
            print("폭탄이 설치되었습니다.")
            return True
        return False

    def die(self, bomb):

        player_x = self.x  # 플레이어 x 좌표
        player_y = self.y  # 플레이어 y 좌표
        bomb = bomb.bomb_range()  # 폭탄 터지는 범위

        if (
                bomb[0] <= player_x <= bomb[1]  # 플레이어 좌표가 폭탄 x좌표 사이에 있다.
                and bomb[3] <= player_y <= bomb[2]  # 플레이어 좌표가 폭탄 y좌표 사이에 있다.
        ):
            return True
        return False

    def activate_shield(self):
        if self.shield_value == 1 and self.die(bomb_instance):  #쉴드가 한 개 있을 때 폭탄에 닿게 되면
            self.shield_value = 0  #쉴드가 0개로 됨
            return True
        return False

    def life(self, bomb):
        if self.die(bomb_instance):
            if self.activate_shield():
                print("쉴드가 사용되었습니다.")
            elif self.life_count > 0:
                self.life_count -= 1
                print(f"목숨 -1, 남은 목숨 {self.life_count}개")
            elif self.life_count == 0:
                self.is_die = True
        return self.life_count


    def use_bomb(self):
        if 5 in self.user_items:
            print("폭탄을 사용합니다.")
            self.user_items.remove(6)
            time.sleep(2)
            self.user_items.append(6)
            print('폭탄이 충전되었습니다.')


    def count(self):
        #Itemlist.user_items.append(name)
        self.b_count += 1
        print("폭탄 개수 증가")  # 중첩 가능
        return self.b_count, 2

    def bomb_range_increase(self):
        result = item_instance.itemlist(value="5")
        if result:
            print("폭탄 범위가 +1 증가되었습니다.")
            bomb_instance.b_range_v += 1
            return True
        return False




    # def user_item(self):
    #    if map_instance.selected_items.value ==


user_instance = User()  #User의 인스턴스
bomb_instance = Bomb(x=3, y=2, user_imf="some_info", ticks=0)
bomb_instance.tick()
item_instance = Itemlist()
map_instance = Map()
# print('{}, {}'.format(map_instance.selected_items.keys, map_instance.selected_items.value))
# print(bomb_instance.bomb_range())
#
# print(user_instance.bomb_range_increase())
# print(bomb_instance.bomb_range())
# print(user_instance.die(bomb_instance))

while True:
    try:
        direction = int(input("이동 방향을 입력하세요 (2: 아래, 4: 왼쪽, 6: 오른쪽, 8: 위쪽, 5: 폭탄 설치): "))
        x_set = user_instance.move_x(direction)
        y_set = user_instance.move_y(direction)

        if user_instance.bomb(direction):
            print("폭탄 좌표: ({}, {})".format(x_set, y_set))
            user_instance.use_bomb()
        else:
            print("현재 좌표: ({}, {})".format(x_set, y_set))

        user_instance.life(bomb_instance)


    except ValueError:
        pass

