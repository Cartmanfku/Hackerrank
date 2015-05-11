
def partition(c,left,right,pivotidx):
    pivot = c[pivotidx]
    storeidx = left
    for i in range(left,right):
        if c[i] > pivot:
            continue
        else:
            c[i],c[storeidx] = c[storeidx],c[i]
            storeidx = storeidx + 1
    else:
        c[storeidx],c[pivotidx] = c[pivotidx],c[storeidx]
    
    return storeidx

def quicksort(c,left,right):
    if left >= right:
        return
    pivotidx = partition(c,left,right,right)
    quicksort(c,left,pivotidx-1)
    quicksort(c,pivotidx+1,right)


def closetnum(c):
    mind = None
    minp = []
    for i in range(0,len(c)-1):
        d = abs(c[i]-c[i+1])
        if mind is None:
            mind = d
            minp = [i]
        elif d < mind:
            mind = d
            minp = [i]
        elif d == mind:
            minp.append(i)
        else:
            continue
    else:
        return minp


n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
quicksort(c, 0, len(c)-1)
minp = closetnum(c)
print ' '.join(['%s %s'%(c[i],c[i+1]) for i in minp])
