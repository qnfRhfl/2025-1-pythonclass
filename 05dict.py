# 2025.04.15 python 강의
# 딕셔너리 (사전)
# 리스트, 배열 -> 딕셔너리

ice = {'메로나':1000, '폴로포':1200, '빵빠레':1800, '죠스바':200}
print(ice['빵빠레'])
ice['메로나'] = 1500
print(ice)
del ice['폴로포']
print(ice)

inventory = {'메로나':[1000, 20], '폴로포':[1200, 5], '빵빠레':[1800, 80], '조스바':[200, 50]}
print(inventory)
print(inventory['메로나'])
print(inventory['메로나'][0])
print(inventory['메로나'][1])
# 딕셔너리 추가
inventory['돼지바'] = [900, 30]
print(inventory)

# 각각의 요소  출력
print(inventory.keys())
print(inventory.values())
print(inventory.items())

# 루프로 각 요소 탐색
for k, v in inventory.items():
    print("키값:", k)
    print("밸류값", v)
