
def cancel(n,k,c):
    for x in c:
        if x <= 0:
            k = k -1
            if k == 0:
                print 'NO'
                return
    else:
        print 'YES'
        



t = int(raw_input())
for i in range(0,t):
    n,k = map(int, raw_input().strip().split(" "))
    c = map(int, raw_input().strip().split(" "))
    cancel(n,k,c)