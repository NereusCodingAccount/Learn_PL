a = input()
b = input()
c = input()
d = input()

# 此為格式化字串的範例
# .format()在print括號裡

print("|%7.2f %7.2f|"%(a,b)) # %7.2f表示寬度為7個字元(7)，小數點後顯示2位(2f)
print("|%7.2f %7.2f|"%(c,d))
print("|{:<7.2f} {:<7.2f}|".format(a,b))
print("|{:<7.2f} {:<7.2f}|".format(c,d))
