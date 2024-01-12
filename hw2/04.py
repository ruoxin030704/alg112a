def power_2n_method4(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

# 測試
n = int(input("請輸入指數 n："))
result = power_2n_method4(n)
print(f"2^{n} 等於 {result}")
