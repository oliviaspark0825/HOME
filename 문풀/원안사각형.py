
r = 4
cnt = 0
for i in range(r):
    for j in range(r):
        if (r-i)**2+(r-j)**2 <= r**2:
            cnt += 1
print(cnt*4)