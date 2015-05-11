
from datetime import datetime


def time_delta(t1, t2):
    d1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z') #%z is supported in python3
    d2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    


T = int(raw_input())
for i in range(0,T):
    t1 = raw_input()
    t2 = raw_input()
    print time_delta(t1, t2)