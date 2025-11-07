num = input().replace("-","") # 移除連字號
if(num.isdigit()): # isdigit() 函數用來檢查字串是否只包含數字
    print('Valid SSN')  
else:
    print('Invalid SSN')
