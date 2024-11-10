text = input("请输入一段英文：")
words = text.split() 
unique_words = set(words)
output_text = " ".join(unique_words)  

print("去重：", output_text)