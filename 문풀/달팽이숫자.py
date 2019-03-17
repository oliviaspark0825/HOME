def  iswall(x,y):
    global N, arr
    # 벽이면 지나가!
    if x<0 or x >= N : return True
    if y<0 or y>=N : return True
    # 이미 방에 숫자가 채워져있음 지나가!
    if arr[x][y] != 0: return True
    return False

import sys
sys.stdin = open('달팽이.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x,y = 0,0
    num = 1
    idx = 0

    while num <= N*N:

        if iswall(x,y) == False:

            arr[x][y] = num
            num += 1

        else:
            x -= dx[idx]
            y -= dy[idx]
            idx = (idx+1) % 4
        x += dx[idx]
        y += dy[idx]

    print('#{}'.format(N))
    for a in range(N):
        for b in range(N):
            print(arr[a][b], end='  ')
        print()
