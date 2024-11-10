text = input("请输入一段英文：")
words = text.split() 

three_letter_words = []  

for word in words:
    if len(word) == 3:  
        three_letter_words.append(word)  

if three_letter_words: 
    print("长度为3个字母的单词有：")
    for word in three_letter_words:
        print(word)
else:
    print("没有长度为3个字母的单词")