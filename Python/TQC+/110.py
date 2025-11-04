import math
n=eval(input())
s=eval(input())
print('Area = %.4f'%((n*s**2)/(4*math.tan(math.pi/n))))
# (n*s^2)/(4*tan(π/n))為正n邊形面積公式
# math.tan()為math模組中的反正切函式
# math.pow()為math模組中的次方函式