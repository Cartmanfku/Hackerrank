

"""
under a sorted array c, to insert c[-1]
"""
def insertion(c):
    r = c[-1]
    for i in reversed(range(1,len(c))):
        if c[i-1] > r:
            c[i] = c[i-1]
            yield c
        else:
            c[i] = r
            yield c
            return 
    else:
        c[0] = r    
        yield c


n = int(raw_input())
c = map(int, raw_input().strip().split(' '))
for x in insertion(c):
    print ' '.join([str(x) for x in c])
