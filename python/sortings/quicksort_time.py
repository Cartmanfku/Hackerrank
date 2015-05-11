
TQ = 0
TI = 0


def partition(c,left,right,pivotidx):
    global TQ
    pivot = c[pivotidx]
    storeidx = left
    for i in range(left,right):
        if c[i] > pivot:
            continue
        else:
            c[i],c[storeidx] = c[storeidx],c[i]
            TQ = TQ + 1
            storeidx = storeidx + 1
    else:
        c[storeidx],c[pivotidx] = c[pivotidx],c[storeidx]
        TQ = TQ + 1
    
    return storeidx

def quicksort(c,left,right):
    if left >= right:
        return
    pivotidx = partition(c,left,right,right)
    quicksort(c,left,pivotidx-1)
    quicksort(c,pivotidx+1,right)
    
def insertion(c):
    global TI     
    for i in range(1,len(c)):
        r = c[i]
        for j in reversed(range(1,i+1)):
            if c[j-1] > r:
                c[j] = c[j-1]
                TI = TI + 1
            else:
                c[j] = r
                break
        else:
            c[0] = r    
    
    
n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
c2 = [x for x in c]
quicksort(c, 0, len(c)-1)
insertion(c2)
print TI - TQ


