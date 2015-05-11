
"""
Check Nesting arguments in https://docs.python.org/2/library/string.html
"""
N = int(raw_input())
width = len(bin(N))-2
for num in range(1,N+1):
    for base in 'doXb':
        print '{0:{width}{base}}'.format(num, base=base, width=width),
    print
    