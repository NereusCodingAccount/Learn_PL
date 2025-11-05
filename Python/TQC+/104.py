import math

r=eval(input("")) # eval()函式可將輸入的字串轉換成數值型態
print("Radius = %.2f"%r) 
print("Perimeter = %.2f"%(r*2*math.pi)) # math.pi表示圓周率π
print("Area = %.2f"%(r*r*math.pi))

# eval()小知識
# int()函式只能將輸入的字串轉換成整數型態
# eval()函式可將輸入的字串轉換成數值型態(整數或浮點數皆可)
# 但安全性較低，建議使用時要特別注意
# ex: eval("__import__('os').system('rm -rf /')")  # 可能會刪除系統檔案