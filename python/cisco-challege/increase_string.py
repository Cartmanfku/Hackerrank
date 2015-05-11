




t = int(raw_input())
for i in range(0,t):
    table = []
    s= raw_input()
    for j in range(0,26):
        row = map(int,raw_input().split(' '))
        table.append(row)
    
    ens = [ord(x)-ord('a') for x in s]
    