
def cutStick(b):
    if len(b) == 0:
        return
    m = min(b)
    left = [x-m for x in b if x-m != 0 ]
    print len(b)
    cutStick(left)

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(' '))
    cutStick(b)