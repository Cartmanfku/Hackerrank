
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
    print ' '.join(map(str,c))
    #print pivotidx
    quicksort(c,left,pivotidx-1)
    quicksort(c,pivotidx+1,right)
    
    



n = int(raw_input())
c = map(int,raw_input().strip().split(' '))
quicksort(c, 0, len(c)-1)