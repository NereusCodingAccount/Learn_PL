xS = set()
yS = set()
print('Enter group X\'s subjects:')
x = input()
while x != 'end':
    xS.add(x) # 向集合加入科目
    x=input()  
print('Enter group Y\'s subjects:')
y = input()
while y != 'end':
    yS.add(y)
    y=input() 
print(sorted(xS.union(yS))) # 聯集 所有科目
print(sorted(yS.intersection(xS))) # 交集 共同科目
print(sorted(yS.difference(xS))) # 差集 x組沒有的科目
print(sorted(yS.symmetric_difference(xS))) # 對稱差集 只有一組有的科目
