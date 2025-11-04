a=input()
b=input()
c=input()
d=input()
print('|{:>5s} {:>5s}|'.format(a,b)) #{:>5s}表示靠右對齊(>)，寬度為5個字元(5s)
print('|{:>5s} {:>5s}|'.format(c,d)) # :s表示字串
print('|{:<5s} {:<5s}|'.format(a,b))
print('|{:<5s} {:<5s}|'.format(c,d))