n = input()
b = 0
for i in range(len(n)):
    if n[i].isupper(): # isupper() 函數用來檢查字元是否為大寫字母
        b=1
if b==1 and len(n)>=8 and n.isalnum(): # isalnum() 函數用來檢查字串是否只包含字母和數字
    print("Valid password")
else:
    print("Invalid password")
