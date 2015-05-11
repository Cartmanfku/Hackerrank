
def partition(c):
    pivot = c[0]
    storeidx = 1
    for i in range(1,len(c)):
        if c[i] >= pivot:
            continue
        else:
            c[i],c[storeidx] = c[storeidx],c[i]
            storeidx = storeidx + 1
    else:
        c[storeidx-1],c[0] = c[0],c[storeidx-1]
    return c



n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
c = partition(c)
print ' '.join(map(str,c))
