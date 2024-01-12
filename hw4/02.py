def solve_equation_newton():
    x0 = 0  # 選擇初始值
    iterations = 0
    max_iterations = 1000
    tolerance = 1e-8  # 允許的誤差範圍

    while iterations < max_iterations:
        f_x = x0**2 - 3*x0 + 1
        f_prime_x = 2*x0 - 3

        if abs(f_x) < tolerance:
            break  # 解已經足夠接近零

        x0 = x0 - f_x / f_prime_x
        iterations += 1

    return x0

result = solve_equation_newton()
print("Newton's method solution:", result)

#參考chatGPT