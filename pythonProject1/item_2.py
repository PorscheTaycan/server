import time
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

class Itemlist:
    user_items = [5,5,6,7,8]                                # 임의의 유저 아이템 리스트
    bomb_list = [1]
    # 폭탄의 default
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
        self.items = []

    def itemlist(self, value):
        if value == "5":  # 아이템 번호가 5번일 경우 리스트에 5 들어가기
            self.items.append(5)
            self.b_range += 1
            return self.b_range
        elif value == "6":  # 아이템 번호가 6번일 경우 리스트에 6 들어가기
            self.items.append(6)
            self.b_count += 1
            print("폭탄 개수 증가")  # 중첩 가능
            return self.b_count
        elif value in ["7", "8"]:
            if int(value) not in self.items:
                # "7" 또는 "8"이 없을 때 실행할 코드
                if value == "7":  # 아이템 번호가 7번일 경우 리스트에 7 들어가기
                    self.user_items.append(7)
                    print("방어")  # 중첩 불가능
                elif value == "8":  # 아이템 번호가 8번일 경우 리스트에 8 들어가기
                    self.user_items.append(8)
                    print("던지기")  # 중첩 불가능

class User:
    def __init__(self):
        self.x = 1
        self.y = -1
        self.has_bomb = False
        self.is_die = False
        self.life_count = 3
        self.items = [] #아이템을 실시간으로 받기
        self.bomb_list = [1]
        self.user_items = [5, 6, 6, 6, 7, 8]

    # def get_list(self):
    #     if (self.x == item x 좌표) and (self.y == item y 좌표):
    #         result = self.items.append()
    #         return result

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
        if direction == 5:
            print("폭탄이 설치되었습니다.")
            self.has_bomb = True
            return True
        return False

    def die(self, bomb):

        player_x = self.x
        player_y = self.y
        bomb = bomb.bomb_range()

        if (bomb[0] <= player_x <= bomb[1] and bomb[3] <= player_y <= bomb[2]):
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

    def activate_shield(self):
        if item_instance.shield_value == 1 and self.die(bomb_instance):  #쉴드가 한 개 있을 때 폭탄에 닿게 되면
            item_instance.shield_value = 0  #쉴드가 0개로 됨
            return True
        return False

    def count(self):
        #Itemlist.user_items.append(name)
        Itemlist.b_count += 1
        print("폭탄 개수 증가")  # 중첩 가능
        return Itemlist.b_count, 2

    def bomb_box(self, bomb1): #폭탄이 담기는 리스트 함수
        for i in range(Itemlist.b_count):
            self.bomb_list.append(bomb1)

    def bomb_use(self): #폭탄을 사용하는 함수
        if Itemlist.b_count > 0:
            use_bomb = self.bomb_list.pop()
            print(f"폭탄 사용:{use_bomb}")
            Itemlist.b_count -= 1
            return use_bomb
        else:
            print("폭탄 부족")
            return None

    def use_bomb(self):
        if 5 in self.user_items:
            print("폭탄을 사용합니다.")
            self.user_items.remove(6)
            time.sleep(2)
            self.user_items.append(6)
            print('폭탄이 충전되었습니다.')

    def bomb_range_increase(self):
        result = item_instance.itemlist(value="5")
        if result:
            print("폭탄 범위가 +1 증가되었습니다.")
            bomb_instance.b_range_v += 1
            return True
        return False

    #def chain(self):

# 초기 좌표 설정
user_instance = User()  #User의 인스턴스
bomb_instance = Bomb(x=3, y=2, user_imf="some_info", ticks=0)
bomb_instance.tick()
item_instance = Itemlist()

while True:
    try:
        direction = int(input("이동 방향을 입력하세요 (2: 아래, 4: 왼쪽, 6: 오른쪽, 8: 위쪽, 5: 폭탄 설치): "))
        x_set = user_instance.move_x(direction)
        y_set = user_instance.move_y(direction)

        if user_instance.bomb(direction):
            print("폭탄 좌표: ({}, {})".format(x_set, y_set))
            if user_instance.die(bomb_instance):
                print("폭탄 범위 안에 있음")
                print(f"목숨 -1, 남은 목숨: {user_instance.life_count}개")
                if user_instance.life(bomb_instance):
                    print("쉴드가 사용되었습니다.")
                print(user_instance.user_items)
                user_instance.use_bomb()
            else:
                print("플레이어가 안전함")
                #print("Game Over")
                #break
        # if : # 5번의 아이템을 먹었을 경우
        #     for i in range(item_instance.b_range):
        #         print(user_instance.bomb_range_increase())
        #         print(bomb_instance.bomb_range())

        else:
            print("현재 좌표: ({}, {})".format(x_set, y_set))

    except:
        pass