#複製chatGPT程式碼，稍微了解但有點不懂
def dfs(maze, start, end):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def dfs_helper(x, y):
        if x == end[0] and y == end[1]:
            return True  #找到目標狀態

        if is_valid(x, y):
            maze[x][y] = -1  #標記已經訪問過的位置

            #嘗試向四個方向進行深度優先搜尋
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                if dfs_helper(x + dx, y + dy):
                    return True

            maze[x][y] = 0  #恢復為未訪問的狀態

        return False

    #起點是否是合法的狀態
    if not is_valid(start[0], start[1]) or not is_valid(end[0], end[1]):
        return None

    #深度優先搜尋的起點
    if dfs_helper(start[0], start[1]):
        return maze
    else:
        return None


maze_example = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

result = dfs(maze_example, start_point, end_point)
if result:
    print("找到路徑：")
    for row in result:
        print(row)
else:
    print("找不到路徑。")
