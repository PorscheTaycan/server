import time
class Bomb:
    def __init__(self, x, y, user_imf, ticks):
        self.x = x
        self.y = y
        self.user_imf = user_imf
        self.ticks = ticks
        self.original_ticks = ticks
        self.user_items = [5, 6, 6, 6, 7, 8]
        self.bomb_list = []
        self.b_range = 3

    def tick(self, external_ticks=None):
        if external_ticks is not None:
            self.ticks = external_ticks

        if self.ticks == self.original_ticks + 4:
            print("폭탄이 터졌습니다!")

        return self.ticks

    def bomb_range(self):
        coordinates = []
        for i in range(-self.b_range, self.b_range + 1):
            if i != 0:
                coordinates.append((self.x + i, self.y))
            else:
                for j in range(-self.b_range, self.b_range + 1):
                    coordinates.append((self.x, self.y + j))
        up, down, left, right = [], [], [], []
        sort_list = []
        for x, y in coordinates:
            if x == self.x and y < self.y:  # 상
                up.append((x, y))
            elif x == self.x and y > self.y:  # 하
                down.append((x, y))
            elif y == self.y and x < self.x:  # 좌
                left.append((x, y))
            elif y == self.y and x > self.x:  # 우
                right.append((x, y))
        up.sort(reverse=True)
        down.sort()
        left.sort(reverse=True)
        right.sort()
        sort_list.append(up)
        sort_list.append(down)
        sort_list.append(left)
        sort_list.append(right)
        return sort_list

    def get_bomb_imf(self):
        return [self.x, self.y, self.user_imf, self.ticks, self.b_range]

    def bomb_count(self):  # 폭탄 개수 증가시키는 함수

        Itemlist.b_count += 1
        print(f"폭탄 개수가 1 증가하여 현재 폭탄 개수는 {Itemlist.b_count}개 입니다.")
        self.bomb_box()
        print(f"폭탄 리스트에 새로운 폭탄이 추가되었습니다. 현재 폭탄 리스트: {self.bomb_list}")  # 주석처리 해야 함. print문으로 폭탄 리스트 갱신되는 거 확인하는 용
        return Itemlist.b_count, 2

    def bomb_box(self):  # 폭탄이 담기는 리스트 함수
        self.bomb_list = [Bomb(self.x, self.y, self.user_imf, self.original_ticks) for i in range(Itemlist.b_count)]

    def use_bomb(self):  # 리스트에 담긴 폭탄 갯수만큼 사용 및 충전
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
            bomb_instance.b_range += 1
            self.bomb_box()
            print(f"폭탄 리스트에 새로운 폭탄이 추가되었습니다. 현재 폭탄 리스트: {self.bomb_list}")  # 주석처리 해야 함. print문으로 폭탄 리스트 갱신되는 거 확인하는 용
            return True
        return False

class Itemlist:
    user_items = [7]                                # 임의의 유저 아이템 리스트
   # bomb_list = ["a", "b", "c"]
    # 폭탄의 default
    a = {"5":"a","6":"b","7":"c","8":"d"}                   # 아이템의 값이 들어있는 리스트


    life = 1  # 우선 라이프로 표현한건데, hp 체력으로 처리해도 될 듯. 데미지 무효,무적 되게 (폭탄 데미지 +1) 이런식의 체력 줘도 될 듯.
    b_range = user_items.count(5)
    b_count = user_items.count(6)
    shield_value = user_items.count(7)
    # 아이템

    def __init__(self):
        # 해당 클래스의 초기화 메서드에서 인스턴스 변수를 초기화하도록 변경
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
    def __init__(self, item_instance):  # 시작 좌표 (1, 1)
        self.x = 1
        self.y = 1
        self.has_bomb = False
        self.is_die = False
        self.life_count = 3
        self.items = []
        self.shield_value = item_instance.user_items.count(7)
        self.b_count = item_instance.b_count

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
            if self.y <= -13:
                self.y = -12
        elif direction == 8:
            self.y += 1  # 위쪽으로 이동
            if self.y >=0:
                self.y = -1
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
        bomb_ranges = bomb.bomb_range()

        for direction_range in bomb_ranges:
            if (
                    direction_range[0][0] <= player_x <= direction_range[-1][0]
                    and direction_range[-1][1] <= player_y <= direction_range[0][1]
            ):
                if self.shield_value > 0:
                    self.shield_value -= 1
                    print("쉴드가 사용되었습니다.")
                    return True
                elif self.life_count > 0:
                    self.life_count -= 1
                    print(f"목숨 -1, 남은 목숨 {self.life_count}개")
                    if self.life_count == 0:
                        self.is_die = True
                        print("Game Over")
                        return False
                return True
        return False





    #def chain(self):
item_instance = Itemlist()
# user_instance = User()  #User의 인스턴스
user_instance = User(item_instance) # User의 인스턴스를 생성할 때 Itemlist 인스턴스를 전달
bomb_instance = Bomb(x=3, y=2, user_imf="some_info", ticks=0)
bomb_instance.tick()
# print(bomb_instance.bomb_range())
# print(bomb_instance.bomb_range_increase())
# print(bomb_instance.bomb_range())
#
# #bomb 갯수 확인
# bomb_instance.bomb_count()
# print(bomb_instance.bomb_list)
# bomb_instance.bomb_count()
# print(bomb_instance.bomb_list)
# bomb_instance.bomb_count()
# print(bomb_instance.bomb_list)

while True:
    try:
        direction = int(input("이동 방향을 입력하세요 (2: 아래, 4: 왼쪽, 6: 오른쪽, 8: 위쪽, 5: 폭탄 설치): "))
        x_set = user_instance.move_x(direction)
        y_set = user_instance.move_y(direction)

        if user_instance.bomb(direction):
            print("폭탄 좌표: ({}, {})".format(x_set, y_set))
            bomb_coordinates = bomb_instance.bomb_range()
            if any((user_instance.x, user_instance.y) in direction_range for direction_range in bomb_coordinates):
                print("폭탄 범위 안에 있음")
                if user_instance.die(bomb_instance):
                    bomb_instance.use_bomb()

                else:
                    # print("Game Over")

                    break
            else:
                pass
        else:
            print("현재 좌표: ({}, {})".format(x_set, y_set))

        #user_instance.life(bomb_instance)


    except ValueError:
        pass