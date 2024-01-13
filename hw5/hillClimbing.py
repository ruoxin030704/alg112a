#修改老師上課範例
import random

def hillClimbing(f, p, h=0.01):
    failCount = 0  #失敗次數歸零
    while failCount < 10000:  #如果失敗次數小於一萬次就繼續執行
        fnow = f(*p)  #fxy 為目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:  #如果移動後高度比現在高
            fnow = f1  #就移過去
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0  #失敗次數歸零
        else:  #若沒有更高
            failCount += 1  #那就又失敗一次
    return p, fnow  #結束傳回（已經失敗超過一萬次了）

def neighbor(f, p, h=0.01): #對p中的每個元素加上一個小的隨機值
    p1 = [x + random.uniform(-h, h) for x in p]
    return p1, f(*p1)

def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

result = hillClimbing(f, [2, 1, 3])
print("Optimal solution:", result[0])
print("Optimal value:", result[1])
