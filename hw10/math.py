# 使用二分法
def solve_polynomial_equation(f, a, b, epsilon=1e-6, max_iterations=1000):
    
    if f(a) * f(b) > 0:
        print("搜索區間內沒有根")
        return None

    for _ in range(max_iterations):
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print("未能在指定的迭代次數內找到解")
    return None

# 範例1: x^5 + 1 = 0
equation1 = lambda x: x**5 + 1
solution1 = solve_polynomial_equation(equation1, -2, 2)
print(f"方程 x^5 + 1 = 0 的解： {solution1}")

# 範例2: x^8 + 3x^2 + 1 = 0
equation2 = lambda x: x**8 + 3*x**2 + 1
solution2 = solve_polynomial_equation(equation2, -2, 2)
print(f"方程 x^8 + 3x^2 + 1 = 0 的解： {solution2}")
