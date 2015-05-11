def count(c):
    cnt = [0 for i in range(0,100)]
    for x in c:
        cnt[x] = cnt[x] + 1
    else:
        return cnt
    
def aggregate(c):
    agg = [0 for i in range(0,100)]
    agg[0] = c[0]
    for i in range(1,100):
        agg[i] = c[i] + agg[i-1]
    else:
        return agg  
    
    
    
n = int(raw_input())
c = []
for i in range(0,n):
    a,b = raw_input().strip().split(' ')
    c.append(int(a))

cnt = count(c)
agg = aggregate(cnt)
print ' '.join(map(str,agg))