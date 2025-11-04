l=[0]*5
l[0]=eval(input())
l[1]=eval(input())
l[2]=eval(input())
l[3]=eval(input())
l[4]=eval(input())
print(l[0],l[1],l[2],l[3],l[4])
print('Sum = %.1f'%sum(l)) # sum()函式可計算數值型態的總和
print('Average = %.1f'%(sum(l)/len(l))) 
