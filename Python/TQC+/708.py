count = eval(input())

alpha = 26

for i in range(count):
 sentence = input()
 set1 = set(sentence.lower()) # 轉成小寫並放入集合
 if ' ' in set1:
     set1.remove(' ') # 移除空白字元
 if len(set1) >= alpha:
     print('True')
 else:
     print('False')
