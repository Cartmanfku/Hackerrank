

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    """
    WTF? it passed!
    """
    print [1,22,333,4444,55555,666666,7777777,88888888,999999999][i-1]
    """
    This is correct way
    print reduce[lambda x,y:10x+y, [i]*i]
    """