# 2025. 04. 29 python 수업 객체지향 프로그래밍 실습
from PIL.ImImagePlugin import number


class SoccerPlayer(object):

    # 생성자 constructor
    # 객체 object가 생성될때 자동 생선
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
        print('init함수가 실행됨')

    def change_back_number(self, new_number):
        print(f'선수 번호 교체: {self.back_number} => {new_number}')
        self.back_number = new_number

    def __str__(self):
        return f"저의 이름은 {self.name}, 위치는 {self.position}, 번호는 {self.back_number} 입니다. 화이팅"

# SoccerPlayer 클래스가 jh 오브젝트를 생성함
# 클래스의 생성함수 constructor가 실행됨
jh = SoccerPlayer("김종현", "MF", 10)

print(jh)

print(jh.name)

jh.change_back_number(5)

print(f'{jh.back_number}')

names = ["Messi", "Ramos", "Ronaldo", "Park", "Son"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 9, 8, 7, 1]

players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

messi = SoccerPlayer(players[0][0], players[0][1], players[0][2])
print(messi.name)

player_oject = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_oject[0])

print(player_oject[0].name)

