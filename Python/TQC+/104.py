import math

r=eval(input("")) # eval()函式可將輸入的字串轉換成數值型態
print("Radius = %.2f"%r) 
print("Perimeter = %.2f"%(r*2*math.pi)) # math.pi表示圓周率π
print("Area = %.2f"%(r*r*math.pi))
