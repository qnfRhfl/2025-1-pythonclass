# 2025.4.2. 파이썬 수업 프로젝트 두번째
# 콜라츠 추측, 또는 도박수
# 1부터 100까지숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙 : n이 짝수 -> n/2
#       n이 홀수 -> 3 * n + 1
#       예: 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)

import numpy as np
import statistics
import time

from p02Collatzfunc import collatz

MAXNUM = 100

# 2025.4.09. 우박수 프로젝트 2번째 : 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량: 평균, 중앙값, 표준편차, 최대값

#리스트 방식

start = time.time()
ncountl = []

for n in range(1,MAXNUM):
    # print(f'{n=}')
    ncount = collatz(n)
    ncountl.append(ncount)


# print(ncountl)
nmax = 0
#최대값, 평균, 중앙값,펴준편차, 최빈값
print(f'최대값={max(ncountl)}')
print(f'해당숫자{ncountl.index(max(ncountl))+1}')
print('두 번째로 큰 값=',sorted(ncountl, reverse=True)[1])
print(f'해당 숫자={ncountl.index(sorted(ncountl, reverse=True)[1])+1}')
print('세 번째로 큰 값=',sorted(ncountl, reverse=True)[2])
print(f'해당 숫자={ncountl.index(sorted(ncountl, reverse=True)[2])+1}')
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl)}')
print(f'표준편차={statistics.stdev(ncountl):.5f}')

end = time.time()
print(f'{end-start:.5f}s')

print(f'                                                   ')
# numpy 방식
start = time.time()

ncounta = np.zeros(MAXNUM-1)
for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncounta[n-1] = ncount
ncounta_sorted=np.argsort(ncounta)
maxval = np.unique(ncounta)
if maxval.size >= 2:
    second_val = maxval[-2]
    third_val = maxval[-3]

print(f'최대값={np.max(ncounta)}')
print(f'해당숫자={np.argmax(ncounta)+1}')
print(f'두 번째로 큰 값 = {second_val}')
print(f'해당 숫자 = {ncounta_sorted[-2]+1}')
print(f'세 번째로 큰 값 = {third_val}')
print(f'해당 숫자 = {ncounta_sorted[-3]+1}')
print(f'평균={np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta)}')
print(f'표준편차={np.std(ncounta):.5f}')
end = time.time()

print(f'{end-start:.5f}s')
