n = str(input(''))
sum = 0
for i in range(0,len(n)):
    sum += ord(n[i]) # ord() 函數用來取得字元(長度為1的) ASCII 碼
    print('ASCII code for \''+n[i]+'\' is '+str(ord(n[i])))
print(sum)

# chr() 函數用來將 ASCII 碼轉成字元(長度為1的)