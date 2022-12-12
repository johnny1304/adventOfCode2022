tv = [[],[],[],[],[],[]]
def rayTube():
    clock = 0
    regCount = 1
    total = 0
    with open("day10/resources/input.txt","r") as file:
        for line in file:
            if line.strip("\n")=="noop":
                clock+=1
                total += draw(clock, regCount)  
            else:
                add = line.strip("\n").split(" ")
                for i in range(0,2):
                    clock+=1
                    total += draw(clock, regCount)
                    print("Adding")
                regCount+=int(add[1])
                print("regCount:"+str(regCount))
    print("Total"+str(total))

def checkClockValue(clock,regCount):
    if clock==20:
        return clock*regCount
    elif clock==60:
        return clock*regCount
    elif clock==100:
        return clock*regCount
    elif clock==140:
        return clock*regCount
    elif clock==180:
        return clock*regCount
    elif clock==220:
        return clock*regCount
    else:
        return 0

def draw(clock,regCount):
    if clock<41:
        line = tv[0]
    elif clock<81:
        line = tv[1]
    elif clock<121:
        line = tv[2]
    elif clock<161:
        line = tv[3]
    elif clock<201:
        line = tv[4]
    else:
        line = tv[5]
        line.append(".")
        line.append("#")
    

if __name__ == "__main__":
    rayTube()