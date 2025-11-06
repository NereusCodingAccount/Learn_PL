total = eval(input())
y = eval(input())
m = eval(input())
print('%s \t  %s' % ('Month', 'Amount'))
for i in range(1, m + 1):
    total += total * y / 1200    
    print(f'{i:3d} \t {total:.2f}') # 設定欄寬為3 # 設定欄寬為.2f
