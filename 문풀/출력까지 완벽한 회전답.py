T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    first = [[0] * N for i in range(N)]
    second = [[0] * N for i in range(N)]
    third = [[0] * N for i in range(N)]
    result = []
    for i in range(N - 1, -1, -1):
        for j in range(N):
            first[j][i] = arr[N - 1 - i][j]

    for i in range(N - 1, -1, -1):
        for j in range(N):
            second[j][i] = first[N - 1 - i][j]

    for i in range(N - 1, -1, -1):
        for j in range(N):
            third[j][i] = second[N - 1 - i][j]

    # 리스트 확장 (extend(x)) x에는 리스트만 올 수 있다.
    result.extend(first)
    result.extend(second)
    result.extend(third)

    # 리스트
    print("#{}".format(tc))
    for i in range(N):
        brr = []
        for j in range(i, N * 3, N * 3 // 3):
            # join을 사용하기위해 result[j]를 str타입으로 바꿔준다.
            # 맵을 사용하면 list안에 주소만들어간다. 그래서 list로 묶어준다.
            brr.append(''.join(list(map(str, result[j]))))
        print(' '.join(brr))