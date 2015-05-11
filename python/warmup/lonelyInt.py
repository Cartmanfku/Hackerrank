#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    for i in range(0,len(a)):
        answer = answer ^ a[i]
    return answer



if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)