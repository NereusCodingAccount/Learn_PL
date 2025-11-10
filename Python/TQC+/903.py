with open("data.txt","a+",encoding = "utf-8") as file: # a+ 表示可讀寫並在檔案末尾新增
    for i in range(5):
        file.write("\n"+input())
    print("Append completed!")
    print("Content of \"data.txt\":")
    file.seek(0) # 將檔案指標移動到開頭
    print(file.read()) # 移動到檔案開頭

