import math

def secure(c1,c2):
    s = 0
    for i in range(c1,c2+1):
        s = s + math.pow(10,i)
    
    if s > math.pow(10,6):
        return True
    else:
        return False


t = int(raw_input())
for i in range(0,t):
    c1,c2 = map(int,raw_input().strip().split(' '))
    if secure(c1,c2):
        print 'YES'
    else:
        print 'NO'