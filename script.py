import random
import os


def main():
    os.system("chcp 65001")
    availableDictionaries = os.listdir("./dictionaries")
    availableDictionaries.remove(".gitkeep")
    availableDictionaries = [el[:-4] for el in availableDictionaries]
    while True:
        print("Please, choose your topik for today!")
        print("Available:")
        for dictionary in availableDictionaries:
            print(dictionary)
        print("----------------")
        file = input("Choose your topic:")
        if file in availableDictionaries:
            data = ""
            right = 0
            wrong = 0
            with open("dictionaries/"+file+".txt", 'r', encoding="utf-8") as f:
                data = f.read().split("\n")

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


if __name__ == "__main__":
    main()
