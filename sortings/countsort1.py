
def count(c,n):
    cnt = [0 for i in range(0,100)]
    for x in c:
        cnt[x] = cnt[x] + 1
    else:
        return cnt



n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
cnt = count(c,n)
print ' '.join(map(str,cnt))
