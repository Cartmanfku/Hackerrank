def count(c,n):
    cnt = [0 for i in range(0,100)]
    for x in c:
        cnt[x] = cnt[x] + 1
    else:
        return cnt
    
def countsort(cnt):
    srt = []
    for i in range(0,100):
        if cnt[i] == 0:
            continue
        else:
            srt.extend([i for j in range(0,cnt[i])])
    else:
        return srt



n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
cnt = count(c,n)
srt = countsort(cnt)
print ' '.join(map(str,srt))