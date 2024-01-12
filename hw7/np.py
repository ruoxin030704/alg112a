#參考hw6程式，chatgpt

import numpy as np
from micrograd import Value, grad

# 定義可微運算子
def f(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# 初始解
initial_solution = [2.0, 1.0, 3.0]

# 使用 micrograd 的 grad 函數計算梯度
def compute_gradient(x):
    x = [Value(v) for v in x]  # 將變數轉換為可微型
    y = f(x)  # 計算目標函數
    y.backward()  # 執行反向傳播
    return np.array([v.grad for v in x])  # 取得梯度值

# 使用梯度下降法進行優化
learning_rate = 0.01
max_iterations = 1000
tolerance = 1e-6

current_solution = initial_solution.copy()

for iteration in range(max_iterations):
    current_value = f(current_solution)
    gradient = compute_gradient(current_solution)

    if np.linalg.norm(gradient) < tolerance:
        break  # 梯度足夠小，視為已收斂

    current_solution = current_solution - learning_rate * gradient

final_solution = np.array([v.item() for v in current_solution])

# 輸出結果
print("最終解：", final_solution)
print("最終值：", f(current_solution).item())