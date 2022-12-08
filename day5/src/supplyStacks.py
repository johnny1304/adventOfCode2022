import queue

def calculateCrates():
    dict = {}
    dict[1] = []
    dict[2] = []
    dict[3] = []
    dict[4] = []
    dict[5] = []
    dict[6] = []
    dict[7] = []
    dict[8] = []
    dict[9] = []
    with open("../resources/crateSource.txt","r") as file:
        count = 1
        for line in file:
            columns = line.strip("\n").split(" ")
            for i in columns:
                dict[count].append(i)
            count+=1

    moveCrates(dict)

def moveCrates(dict):
    with open("../resources/input.txt","r") as file:
        for line in file:
            moves = line.strip("\n").split(" ")
            movedCrates = []
            for i in range(0,int(moves[0])):
               movedCrates.append(dict[int(moves[1])].pop())

            while len(movedCrates)>0:
                dict[int(moves[2])].append(movedCrates.pop())

    print(dict.get(1).pop())
    print(dict.get(2).pop())
    print(dict.get(3).pop())
    print(dict.get(4).pop())
    print(dict.get(5).pop())
    print(dict.get(6).pop())
    print(dict.get(7).pop())
    print(dict.get(8).pop())
    print(dict.get(9).pop())


if __name__=="__main__":
    calculateCrates()