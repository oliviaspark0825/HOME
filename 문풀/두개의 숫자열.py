import sys
sys.stdin = open('숫자열.txt')
T = int(input())
for tc in range(T):
    a,b = list(map(int,input().split()))
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))
    max = -98765

    if  a<b:
        for i in range(b-a+1):
            multi = 0
            for j in range(a):
                multi += N[j] *M[i+j]
            if max < multi:
                max = multi
    else:
        for i in range(a-b+1):
            multi = 0
            for j in range(b):
                multi += M[j] *N[i+j]
            if max < multi:
                max = multi

    print('#{} {}'.format(tc+1,max))
