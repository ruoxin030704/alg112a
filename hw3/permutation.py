def permutations(arr):
    result = []
    generate_permutations(arr, 0, result)
    return result

def generate_permutations(arr, index, result):
    if index == len(arr):
        result.append(arr.copy())
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]  
        generate_permutations(arr, index + 1, result)
        arr[index], arr[i] = arr[i], arr[index]  

my_list = [1, 2, 3]
all_permutations = permutations(my_list)
print(all_permutations)

#permutations函式接收一個列表arr並返回其所有排列的列表。
#generate_permutations 函式是一個遞迴輔助函式，使用交換的方式生成排列。
#當index達到列表的長度時，它將目前的排列加入到結果中。
#參考chatGPT寫出