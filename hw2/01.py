def power_2n_method1(n):
    result = 2 ** n
    return result

# 測試
n = int(input("請輸入指數 n："))
result = power_2n_method1(n)
print(f"2^{n} 等於 {result}")