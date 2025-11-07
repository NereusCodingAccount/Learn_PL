x = {}
y = {}
print('Create dict1:')
while True:
    key = input('Key: ')
    if key == 'end':
        break
    x[key] = input('Value: ')
print('Create dict2:')
while True:
    key = input('Key: ')
    if key == 'end':
        break
    y[key] = input('Value: ')
x.update(y) # 合併兩個字典
for i in sorted(x.keys()): # 對字典的鍵排序後列出
    print(i+": "+x[i])
