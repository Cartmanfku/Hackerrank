

def bar(x):
    if x%2 == 0:
        return (x/2)*(x/2)
    else:
        return (x/2)*(x/2+1)



t = int(raw_input())
for i in range(0,t):
    x = int(raw_input())
    print bar(x)
    