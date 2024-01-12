def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    return fib_list

n = int(input("請輸入費氏數列的項數："))
result = fibonacci(n)
print(f"前 {n} 項費氏數列為：{result}")