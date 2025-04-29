# 2025. 04. 29 python 수업 객체지향 프로그래밍 실습

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

# SoccerPlayer 클래스가 jh 오브젝트를 생성함
# 클래스의 생성함수 constructor가 실행됨
jh = SoccerPlayer("김종현", "MF", 10)

print(jh)

print(jh.name)

jh.change_back_number(5)

print(f'{jh.back_number}')