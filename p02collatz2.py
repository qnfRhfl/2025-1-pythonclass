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
nmax = 0

for n in range(1,MAXNUM):
    # print(f'{n=}')
    ncount = collatz(n)
    ncountl.append(ncount)


# print(ncountl)

#최대값, 평균, 중앙값,펴준편차, 최빈값
print(f'최대값={max(ncountl):.5f}')
print(f'해당숫자{ncountl.index(max(ncountl))}')
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl):.5f}')
print(f'표준편차={statistics.stdev(ncountl):.5f}')

end = time.time()
print(f'{end-start:.5f}s')

# numpy 방식
start = time.time()
ncounta = np.zeros(MAXNUM-1)
for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncounta[n-1] = ncount


print(f'최대값={np.max(ncounta):.5f}')
print(f'해당숫자={np.max(ncounta):.5f}')
print(f'평균={np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta):.5f}')
print(f'표준편차={np.std(ncounta):.5f}')

end = time.time()
print(f'{end-start:.5f}s')
