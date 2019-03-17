def wall(x,y):
    if x<0 or x >= n:
        return True
    if y<0 or y >= n:
        return True
    if arr[x][y] != 0:
        return True
    return False



import sys
sys.stdin = open('줄세우기.txt')
n = int(input())
arr = [[0 for  _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위쪽
dy = [1, 0, -1, 0]

number = 1
x = 0
y = 0
k = 0
while  number <= n*n:
    if wall(x,y) == False: # 벽이 아니고 값이 없으면 차례로 추가
        arr[x][y] = number
        number += 1
    else:
        x -= dx[k]
        y -= dy[k]
        k = (k+1)%4


    x += dx[k]
    y += dy[k]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()



