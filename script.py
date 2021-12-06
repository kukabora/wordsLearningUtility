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
            correctAnswer = ""
            yourAnswer = ""
            amountOfWords = len(data)
            while True:
                print(f"RIGHT - {right}. WRONG - {wrong}")
                print("Correct answer: " + correctAnswer)
                print("Your answer: " + yourAnswer)
                print("----------------------------")
                index = random.randint(0, amountOfWords-1)
                dic = data[index].split(":")
                indexWord = random.randint(0, 1)
                print(dic[indexWord]+":", end="")
                indexWord = 1 - indexWord
                yourAnswer = input()
                if (dic[indexWord] == yourAnswer):
                    right += 1
                else:
                    wrong += 1
                correctAnswer = dic[0] + ":" + dic[1]
                # os.system('CLS')
                os.system('clear')
        else:
            print("There is no such a dictionary!")


if __name__ == "__main__":
    main()
