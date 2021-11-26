import random
import os
data = ""
with open("dictionary.txt", 'r', encoding="utf-8") as f:
    data = f.read().split("\n")


os.system("chcp 65001")

right = 0
wrong = 0

amountOfWords = len(data)
while True:
    print(f"RIGHT - {right}. WRONG - {wrong}")
    print("----------------------------")
    index = random.randint(0, amountOfWords-1)
    dic = data[index].split(":")
    indexWord = random.randint(0, 1)
    print(dic[indexWord]+":", end="")
    indexWord = 1 - indexWord
    if (dic[indexWord] == input()):
        right += 1
    else:
        wrong += 1
    os.system('CLS')
