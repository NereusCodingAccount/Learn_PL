a=input()
b=input()
c=input()
d=input()
print(f'|{a:>5s} {b:>5s}|') #{:>5s}表示靠右對齊(>)，寬度為5個字元(5s)
print(f'|{c:>5s} {d:>5s}|') # :s表示字串
print(f'|{a:<5s} {b:<5s}|')
print(f'|{c:<5s} {d:<5s}|')

# Format:
# s 字串
# d 十進位整數
# x 十六進位整數
# o 八進位整數
# x 二進位整數
# f 十進位浮點數
# > 靠右對齊
# < 靠左對齊
# ^ 置中對齊



