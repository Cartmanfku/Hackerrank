
def insertion(c):
    
    for i in range(1,len(c)):
        r = c[i]
        for j in reversed(range(1,i+1)):
            if c[j-1] > r:
                c[j] = c[j-1]
            else:
                c[j] = r
                yield c
                break
        else:
            c[0] = r    
            yield c
            


n = int(raw_input())
c = map(int, raw_input().strip().split(' '))
for x in insertion(c):
    print ' '.join([str(x) for x in c])
