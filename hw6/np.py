#了解過內容還是不太理解，複製chatGPT
import numpy as np

def df(f, p, k, step=0.01):
    """計算函數 f 對變數 p[k] 的偏微分"""
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

def grad(f, p, step=0.01):
    """計算函數 f 在點 p 上的梯度"""
    gp = np.zeros_like(p)
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

def gradientDescent(f, initial_point, learning_rate=0.1, tolerance=1e-5, max_iter=1000):
    """使用梯度下降法找到向量函數的谷底"""
    p = initial_point
    for i in range(max_iter):
        gradient = grad(f, p)
        p = p - learning_rate * gradient  # 更新參數
        if np.linalg.norm(gradient) < tolerance:
            print(f"Converged after {i+1} iterations.")
            break
    else:
        print("Did not converge within the maximum number of iterations.")

    return p, f(p)

# 舉例使用的目標函數
def example_function(p):
    return p[0]**2 + p[1]**2 + p[2]**2

# 設定初始點
initial_point = np.array([1.0, 2.0, 3.0])

# 使用梯度下降法找到谷底
result = gradientDescent(example_function, initial_point)

# 印出結果
print("Optimal solution:", result[0])
print("Optimal value:", result[1])
