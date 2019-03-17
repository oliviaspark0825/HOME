import sys
sys.stdin = open('소인수분해.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0,0,0,0,0
    while N != 1:
        if N % 2 ==0:
            a += 1
            N = N//2
        if N % 3 ==0:
            b += 1
            N = N // 3
        if N % 5 ==0:
            c += 1
            N = N // 5
        if N % 7 ==0:
            d += 1
            N = N // 7
        if N %11 ==0:
            e += 1
            N = N // 11
    print ('#{} {} {} {} {} {} '.format(tc+1, a, b, c, d, e))

