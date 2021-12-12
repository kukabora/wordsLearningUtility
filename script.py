import random
import os


def main():
    os.system("chcp 65001")
    availableDictionaries = os.listdir("./dictionaries")
    availableDictionaries.remove(".gitkeep")
    availableDictionaries = [el[:-4] for el in availableDictionaries]
    while True:
        print("Please, choose your topic for today or type 'all' to learn all of your words in dictionaries!")
        print("Available:")
        for dictionary in availableDictionaries:
            print(dictionary)
        print("----------------")
        file = input(
            "Choose your topics (write them down separated by space):")
        check = True
        for dictionaryName in file.split(" "):
            if (not dictionaryName in availableDictionaries):
                check = False
                break
        if check:
            data = []
            right = 0
            wrong = 0
            if file == "all":
                for dictionary in availableDictionaries:
                    with open("dictionaries/"+dictionary+".txt", 'r', encoding="utf-8") as f:
                        data.append(f.read().split("\n"))
            else:
                file = file.split(" ")
                for filename in file:
                    with open("dictionaries/"+filename+".txt", 'r', encoding="utf-8") as f:
                        data.append(f.read().split("\n"))
            correctAnswer = ""
            yourAnswer = ""
            while True:
                amountOfDictionaries = len(data)
                print(f"RIGHT - {right}. WRONG - {wrong}")
                print("Correct answer: " + correctAnswer)
                print("Your answer: " + yourAnswer)
                print("----------------------------")
                currentDictionaryIndex = random.randint(
                    0, amountOfDictionaries-1)
                amountOfWords = len(data[currentDictionaryIndex])
                index = random.randint(0, amountOfWords-1)
                dic = data[currentDictionaryIndex][index].split(":")
                indexWord = random.randint(0, 1)
                print(dic[indexWord]+":", end="")
                indexWord = 1 - indexWord
                yourAnswer = input()
                if (dic[indexWord] == yourAnswer):
                    right += 1
                else:
                    wrong += 1
                correctAnswer = dic[0] + ":" + dic[1]
                os.system('clear')
        else:
            print("There is no such a dictionary!")


if __name__ == "__main__":
    main()
