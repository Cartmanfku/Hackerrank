
def merge(left, right):
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n][0] <= right[m][0]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result


def sort(seq):
    if len(seq) <= 1:
        return seq

    middle = int(len(seq) / 2)
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)


N,M = map(int, raw_input().split(' '))
xin = []
for i in range(0,N):
    x = map(int, raw_input().split(' '))
    xin.append(x)
    
K = int(raw_input())
kin = []
for i in range(0,N):
    kin.append((xin[i][K],i))
    
kin = sort(kin) #cannot use quicksort, it's not stable
for i in range(0, N):
    print ' '.join(map(str,xin[kin[i][1]]))
    