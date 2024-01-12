def solve_equation_bruteforce():
    solutions = []
    for x in range(-100, 101):  
        if x**2 - 3*x + 1 == 0:
            solutions.append(x)
    return solutions

result = solve_equation_bruteforce()
print("Bruteforce solutions:", result)

#參考chatGPT