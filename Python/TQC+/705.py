set1 = set()
set2 = set()
set3 = set()

# 清單能用 + 合併，集合則用 .union() 方法

print('Input to set1:')
for i in range(5):
    set1.add(eval(input())) # add() 方法向集合加入元素
    
print('Input to set2:')
for i in range(3):
    set2.add(eval(input()))
    
print('Input to set3:')
for i in range(9):
    set3.add(eval(input()))
    
print('set2 is subset of set1:',str(set2.issubset(set1))) # issubset() 方法判斷子集合
print('set3 is superset of set1:',str(set3.issuperset(set1))) # issuperset() 方法判斷超集合

# 集合
# 如果集合A的元素都是集合B的元素(∀x)(x∈A → x∈B)，則稱集合A是集合B的子集合，記作A⊆B，或B是A的超集合，記作B⊇A。