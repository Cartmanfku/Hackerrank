

def panlindromes(s):
    count = 0
    for i in range(0,len(s)/2):
        """
        https://docs.python.org/2/library/functions.html#ord
        """
        count = count + abs(ord(s[i])-ord(s[-i-1]))
    else:
        return count
            

t = int(raw_input())
for i in range(0,t):
    s = str(raw_input())
    print panlindromes(s)
    