n = str(input(''))
for i in range(0,len(n)):
    print('Index of \''+n[i]+'\': '+str(i)) # \' 轉義字元成單引號 # \" 為雙引號

    # r'' 代表原始字串(raw string)，不會轉義特殊字元
