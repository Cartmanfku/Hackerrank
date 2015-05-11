
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
    
    

def query_all(f, fl, q, ql):
    if fl < ql:
        return False
    if f[0] > q[0] or f[-1] < q[-1]:
        return False
    i = 0
    j = 0
    n = 0
    while j < ql and i < fl:
        if f[i] == q[j]:
            i = i + 1
            j = j + 1
            n = n + 1
        elif f[i] > q [j]:
            j = j + 1
        else:
            i = i + 1
              
    return n == ql

def query_any(f,fl, q, ql):
    if f[0] > q[-1] or f[-1] < q[0]:
        return False
    i = 0
    j = 0
    while j < ql and i < fl:
        if f[i] == q[j]:
            return True
        elif f[i] > q[j]:
            j = j + 1
        else:
            i = i + 1
    return False

def query_some(f,fl,q,ql):
    if f[0] > q[-1] or f[-1] < q[0]:
        return False
    i = 0
    j = 0
    n = 0
    while j < ql and i < fl:
        if f[i] == q[j] :
            i = i + 1
            j = j + 1
            n = n + 1
        elif f[i] > q [j]:
            j = j + 1
        else:
            i = i + 1
                   
    return n > 0 and n < ql  
        


def query_match(f, fl, q, ql, t):
    if t == 1:
        return query_all(f, fl, q, ql)
    elif t == 2:
        return query_any(f, fl, q, ql)
    elif t == 3:
        return query_some(f, fl, q, ql)
    else:
        return False


def search(files,query):
    s = 0
    for f in files:
        if query_match(f[1:],f[0], query[2:],query[1],query[0]):
            s = s + 1
    else:
        return s
        


t = int(raw_input())
files = []
for i in range(0,t):
    c = map(int,raw_input().strip().split(' '))
    files.append(c)
    
for f in files:
    quicksort(f,1,f[0])
    
t = int(raw_input())
queries = []
for i in range(0,t):
    c = map(int,raw_input().strip().split(' '))
    queries.append(c)
    
for q in queries:
    quicksort(q, 2, q[1]+1)
    
for i in range(0,t):
    print search(files,queries[i])
    
    