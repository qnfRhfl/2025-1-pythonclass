import numpy as np

# 1. 학습 함수
def fit_decision_tree(X, y, max_depth=3):
    """트리를 학습하여 반환"""
    return _build_tree(X, y, depth=0, max_depth=max_depth)

# 트리 생성 (재귀)
def _build_tree(X, y, depth, max_depth):
    if depth >= max_depth or len(set(y)) == 1:
        return np.mean(y)

    best_feature, best_threshold = _find_best_split(X, y)
    if best_feature is None:
        return np.mean(y)

    left_idx = X[:, best_feature] <= best_threshold
    right_idx = X[:, best_feature] > best_threshold

    left_subtree = _build_tree(X[left_idx], y[left_idx], depth + 1, max_depth)
    right_subtree = _build_tree(X[right_idx], y[right_idx], depth + 1, max_depth)

    return {
        'feature': best_feature,
        'threshold': best_threshold,
        'left': left_subtree,
        'right': right_subtree
    }

# 최적 분할 찾기
def _find_best_split(X, y):
    m, n = X.shape
    best_mse = float('inf')
    best_feature, best_threshold = None, None

    for feature in range(n):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_idx = X[:, feature] <= threshold
            right_idx = X[:, feature] > threshold

            if len(y[left_idx]) == 0 or len(y[right_idx]) == 0:
                continue

            mse = _calculate_mse(y[left_idx], y[right_idx])

            if mse < best_mse:
                best_mse = mse
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold

# 평균 제곱 오차(MSE) 계산
def _calculate_mse(left_y, right_y):
    def mse(y):
        return np.mean((y - np.mean(y)) ** 2) if len(y) > 0 else 0
    total_len = len(left_y) + len(right_y)
    return (len(left_y) * mse(left_y) + len(right_y) * mse(right_y)) / total_len

# 2. 예측 함수
def predict_decision_tree(tree, X):
    return np.array([_predict_sample(tree, x) for x in X])

# 한 샘플에 대해 트리 탐색
def _predict_sample(tree, x):
    if not isinstance(tree, dict):
        return tree

    if x[tree['feature']] <= tree['threshold']:
        return _predict_sample(tree['left'], x)
    else:
        return _predict_sample(tree['right'], x)
