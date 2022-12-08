def cleanCamp():
    total=0
    with open("../resources/input.txt","r") as file:
        for line in file:
            inputs = line.strip("\n").split(",")
            elf1 = inputs[0].split("-")
            elf2 = inputs[1].split("-")
            if checkContains(int(elf1[0]),int(elf1[1]),int(elf2[0]),int(elf2[1])):
                total+=1
    print(total)


def checkContains(first1,first2,second1,second2):
        if first1<=second1 and first2>=second2:
            return True
        elif second1<=first1 and second2>=first2:
            return True
        elif first2>=second1 and first2<=second2:
            return True
        elif first1>=second1 and first1<=second2:
            return True
        elif second1>=first1 and second1<=first2:
            return True
        elif second2>=first1 and second2<=first2:
            return True
        else:
            False

if __name__=="__main__":
    cleanCamp()