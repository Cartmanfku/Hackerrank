

def max_subarray(a,l):
    pass

def max(a,l):
    current_i = 0;
    for i in range(0,l):
        pass


t = int(raw_input())
for i in range(0,t):
    l = int(raw_input())
    a = map(int,raw_input().split(' '))
    print max_subarray(a, l),max(a,l)