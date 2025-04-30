# 2025 4. 30 python 수업
# bmi 예측 머신 러닝 에서 객체 지향 실습
from random import random

import numpy as np

np.random.seed(42)

height = np.random.normal(170, 10, 1000)
weight = np.random.normal(65, 15, 1000)
bmi = weight / (height/100) ** 2

x = np.vstack((height, weight)).T
y = bmi

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state=42)

# 1. 함수를 이용한 머신 러닝
# 데이터 를 train 용과 test(30%)용으로 나눔
'''
from p04bmifunctions import fit_decision_tree, predict_decision_tree
#학습 훈련 train
tree_model = fit_decision_tree(x_train, y_train,)
# 테스터 데이터 로 예측
y_pred = predict_decision_tree(tree_model, x_test)
'''

# 2. 자체 제작 클래스 를 이용한 머신 러닝

'''
from p04bmiclass import MyDecisionTree
tree = MyDecisionTree(3)
tree.fit(x_train, y_train)
y_pred = tree.predict(x_test)

'''
# 3. 남이 만들어 놓은 클래스 (DecisionTreeRegressor)를 이용한 머신러닝
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(x_train, y_train)
y_pred = tree.predict(x_train)

# 평가 : 예측된 결과와, 정답 결과 비교

from sklearn.metrics import mean_squared_error

# mse = mean_squared_error(y_pred, y_test)
# print(f"평균제곱오차(MSE):{mse:.3f}")

# 일부 출력
for i in range(5):
    print(f"실제 BMI:     {y_test[i]:.2f} | 예측 BMI: {y_pred[i]:.2f}")