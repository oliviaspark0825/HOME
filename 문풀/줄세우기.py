import sys
sys.stdin = open('줄세우기.txt')
n = int(input())
data = list(map(int,input().split()))
order = [0 for _ in range(n+1)]
print(data)
order[-1] = 1
for i in range(1,n+1):
    if order[-1-data[i]]:
        order[-1-data[i]-1] = order[-1-data[i]]
        order[-1-data[i]] = i+1
print(order)
