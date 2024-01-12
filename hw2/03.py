def power_2n_method3(n):
    if n == 0:
        return 1
    else:
        return 2 * power_2n_method3(n - 1)

# 測試
n = int(input("請輸入指數 n："))
result = power_2n_method3(n)
print(f"2^{n} 等於 {result}")
