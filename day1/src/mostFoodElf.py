import operator


def calculateElfMostFood():
    dict = {}
    finalValue=0
    with open("../resources/input.txt","r") as file:
        total = 0
        elf = 1
        for line in file:
            if line == "\n":
                dict[elf]=total
                total=0
                elf+=1
            else:
                total+=int(line)
    for i in range(0,3):
        maxElf = max(dict, key=dict.get)
        finalValue+=dict[maxElf]
        print(maxElf)
        dict.pop(maxElf)
    print(finalValue)
if __name__== "__main__":
    calculateElfMostFood()