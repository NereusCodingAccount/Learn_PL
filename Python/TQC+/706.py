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

"""
def is_pangram(sentence):
    # 將句子轉換為小寫並移除空格
    sentence = sentence.lower().replace(" ", "")
    # 建立一個包含所有英文字母的集合
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # 建立包含句子中所有字母的集合
    sentence_letters = set(sentence)
    # 比較兩個集合是否相同
    return alphabet.issubset(sentence_letters)

# 範例
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))

"""