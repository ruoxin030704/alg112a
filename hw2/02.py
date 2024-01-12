def power_2n_method2(n):
    result = 1 << n
    return result

# 測試
n = int(input("請輸入指數 n："))
result = power_2n_method2(n)
print(f"2^{n} 等於 {result}")
