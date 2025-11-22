a = float(input())
b = float(input())
c = float(input())
d = float(input())

# 此為格式化字串的範例
# .format()在print括號裡

print(f"|{a:7.2f} {b:7.2f}|") # %7.2f表示寬度為7個字元(7)，小數點後顯示2位(2f)
print(f"|{c:7.2f} {d:7.2f}|")
print("|{:<7.2f} {:<7.2f}|".format(a,b))
print("|{:<7.2f} {:<7.2f}|".format(c,d))
