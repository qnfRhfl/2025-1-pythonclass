# 2025.4.2. 파이썬 수업 프로젝트 두번째
# 콜라츠 추측, 또는 도박수
# 1부터 100까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙 : n이 짝수 -> n/2
#       n이 홀수 -> 3 * n + 1
#       예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)

n = 9

# 단계의 갯수를 셀것 - done
# n을 1부터 99 까지 변화하면서, 각각의 단계수를 출력할 것
# 그 중 가장 큰 수를 찾을 것

maxvalue = -999
maxvalue_s = -999
maxvalue_t = -999
maxvalue_n = 0
maxvalue_ns = 0
maxvalue_nt = 0

for n in range(1,100):
    # print(f'{n=}')
    ncount = 0
    i = n

    while i!=1:
        if  i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i/2
        ncount = ncount + 1

    print(f'{ncount}')
    if maxvalue < ncount:
        maxvalue_t = maxvalue_s
        maxvalue_s = maxvalue
        maxvalue = ncount
        maxvalue_nt = maxvalue_ns
        maxvalue_ns = maxvalue_n
        maxvalue_n = n
    elif maxvalue_s < ncount:
        maxvalue_s = ncount
    elif maxvalue_t < ncount:
        maxvalue_t = ncount





print(f'{maxvalue_n=},{maxvalue=}')
print(f'{maxvalue_ns=},{maxvalue_s=}')
print(f'{maxvalue_nt=},{maxvalue_t=}')