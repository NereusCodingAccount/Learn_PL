n=str(input())
if n.isdigit(): # isdigit()判斷數字
    print(f'{n} is a number.')
elif n.isalpha(): # isalpha()判斷字母
    print(f'{n} is an alphabet.')
else:
    print(f'{n} is a symbol.')
