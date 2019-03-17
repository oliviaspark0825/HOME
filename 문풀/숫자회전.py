# def turn(n):
#     global arr
#     new_arr = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#                 new_arr[i][j] = arr[n-j-1][i]
#
#     arr = new_arr
#     return arr

import sys
sys.stdin = open('숫자회전.txt')
T = int(input())
for tc in range(1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    turn_90 = [[0]*n for _ in range(n)]
    turn_180 = [[0]*n for _ in range(n)]
    turn_270 = [[0]*n for _ in range(n)]
    ans = []

# # 원래 배열의 1열이 90도 회전된 배열에선 1 행이니까
    for i in range(n):
        for j in range(n):
                turn_90[i][j] = arr[n-j-1][i]

    for i in range(n):
        for j in range(n):
                turn_180[i][j] = turn_90[n-j-1][i]

    for i in range(n):
        for j in range(n):
                turn_270[i][j] = turn_180[n-j-1][i]

    ans.extend(turn_90)
    ans.extend(turn_180)
    ans.extend(turn_270)

    print(f'#{tc+1}')
    for i in range(n):
        brr = []
        for j in range(i, n * 3, n* 3 // 3):
            # join을 사용하기위해 result[j]를 str타입으로 바꿔준다.
            # 맵을 사용하면 list안에 주소만들어간다. 그래서 list로 묶어준다.
            brr.append(''.join(list(map(str, ans[j]))))
        print(' '.join(brr))