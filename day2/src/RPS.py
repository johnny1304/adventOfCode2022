
def calculateRPS():
    total = 0
    values = {"A":1,"X":0,"B":2,"Y":3,"C":3,"Z":6}
    with open("../resources/input.txt","r") as file:
        for line in file:
            inputs = line.split(" ")
            opponent = values[inputs[0]]
            yourMove = values[inputs[1].strip("\n")]
            print(yourMove)
            roundMoves = yourMove+opponent
            if opponent == 1:
                if roundMoves == 7:
                    total+=8
                elif roundMoves == 4:
                    total+=4
                else:
                    total+=3
            elif opponent == 2:
                if roundMoves == 8:
                    total+=9
                elif roundMoves == 5:
                    total+=5
                else:
                    total+=1
            elif opponent == 3:
                if roundMoves == 9:
                    total+=7
                elif roundMoves == 6:
                    total+=6
                else:
                    total+=2
    print(total)





if __name__== "__main__":
    calculateRPS()