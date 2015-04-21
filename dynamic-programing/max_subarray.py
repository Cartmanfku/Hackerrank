

def max_subarray(a,l):
    current_sum = 0
    current_idx = -1
    best_sum = 0
    best_start_idx = -1
    best_end_idx = -1
    max_val = a[0]
    for i in range(0,l):
        if a[i] > max_val:
            max_val = a[i]
            
        val = current_sum + a[i]
        if val > 0:
            if current_sum == 0:
                current_idx = i
            current_sum = val
        else:
            current_sum = 0
            
        if current_sum > best_sum:
            best_sum = current_sum
            best_start_idx = current_idx
            best_end_idx = i

    else:
        if best_sum > 0:
            return best_sum
        else:
            return max_val

def max_nonarray(a,l):
    best_sum = 0
    max_val = a[0]
    for i in range(0,l):
        if a[i] > max_val:
            max_val = a[i]
        if a[i] > 0:
            best_sum = best_sum + a[i]
    else:
        if best_sum > 0:
            return best_sum
        else:
            return max_val

t = int(raw_input())
for i in range(0,t):
    l = int(raw_input())
    a = map(int,raw_input().split(' '))
    print max_subarray(a, l),max_nonarray(a,l)
    
    
    
    
    