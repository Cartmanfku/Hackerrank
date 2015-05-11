

def panlindromes(s):
    for i in range(0,len(s)/2):
        """
        https://docs.python.org/2/library/functions.html#ord
        """
        if ord(s[i]) != ord(s[-i-1]):
            return False
    else:
        return True
    
    
def pairblock(a,b):
    if panlindromes(a+b) or panlindromes(b+a):
        return True
    else:
        return False
    

def build(s,t):
    pair = []
    for i in range(0,t):
        p = []
        for j in range(i+1,t):
            if pairblock(s[i],s[j]):
                p.append(j)
        pair.append(p)
                
    return pair   

                        
def minpair(pair, idx, mark):
    if len(pair) == 1:
        if mark[idx] == False:
            return 1
        else:
            return 0
    m = [1+minpair(pair,idx+1,mark)]
    p = pair[idx]
    for i in p:
        if mark[i] == True:
            continue
        mark[i] = True
        m.append(1+minpair(pair,idx+1,mark))
        mark[i] = False
    return min(m)   


x = raw_input()
while x != '':
    try:
        t = int(x)
        s = []
        for i in range(0,t):
            s.append(raw_input())
        pair = build(s,t)
        print minpair(pair,0,[False for i in range(0,t)])
        x = raw_input()
    except EOFError:
        break
        

    
    