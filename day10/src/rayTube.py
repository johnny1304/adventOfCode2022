tv = [[""]*40,[""]*40,[""]*40,[""]*40,[""]*40,[""]*40]
def rayTube():
    clock = -1
    regCount = 1
    total = 0
    with open("day10/resources/input.txt","r") as file:
        for line in file:
            if line.strip("\n")=="noop":
                clock+=1
                draw(clock, regCount)  
            else:
                add = line.strip("\n").split(" ")
                for i in range(0,2):
                    clock+=1
                    draw(clock, regCount)
                    # print("Adding")
                    # print(tv)
                regCount+=int(add[1])
                # print("regCount:"+str(regCount))
    for line in tv:
        print(str(line)+"\n")

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
    print("clock: "+str(clock))
    print("clock mod: "+str(clock%40))
    print("regCount: "+str(regCount))
    
    if clock<40:
        clock=clock%40
        line = tv[0]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    elif clock<81:
        clock=clock%40
        line = tv[1]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    elif clock<121:
        clock=clock%40
        line = tv[2]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    elif clock<161:
        clock=clock%40
        line = tv[3]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    elif clock<201:
        clock=clock%40
        line = tv[4]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    else:
        clock=clock%40
        line = tv[5]
        if regCount==clock-1 or regCount==clock or regCount==clock+1:
            line[clock] = "#"
            
        else:
            line[clock] = "."
    

if __name__ == "__main__":
    rayTube()