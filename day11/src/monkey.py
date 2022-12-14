import queue
import re
import math

def monkey():
    items = [queue.Queue() for i in range(0,8) ]
    operations = [""]*8
    tests = [0]*8
    trueAction = [0]*8
    falseAction = [0]*8
    itemCount = [0]*8
    count=-1
    with open("day11/resources/input.txt","r") as file:
        for line in file:
            if re.match("Monkey "+str(count+1)+":.*",line):
                count+=1
            elif re.match(".*Starting items:.*",line):
                for item in re.findall("[0-9]+",line):
                    items[count].put(int(item))
            elif re.match(".*Operation:.*",line):
                words = line.strip("\n").split(" ")
                operations[count]=words[-2]+words[-1]
            elif re.match(".*Test: divisible by.*",line):
                testValue = line.strip("\n").split(" ")
                tests[count] = int(testValue[-1])
            elif re.match(".*If true: throw to monkey.*",line):
                monkeyValue = line.strip("\n").split(" ")
                trueAction[count] = int(monkeyValue[-1])
            elif re.match(".*If false: throw to monkey.*",line):
                monkeyValue = line.strip("\n").split(" ")
                falseAction[count] = int(monkeyValue[-1])
    for i in range(0,4):
        print("items" +str(items[i].queue))
        print("tests: "+str(tests[i]))
        print("operations: "+str(operations[i]))
        print("\n")
    for _ in range(0,10000):
        count=0
        while count<8:
            while not items[count].empty():
                itemCount[count]+=1
                item = items[count].get()  
                worry = getOperation(operations[count],item)
                # worry = math.floor(worry / 3)
                if worry%tests[count]==0:
                    items[trueAction[count]].put(worry)
                else:
                    items[falseAction[count]].put(worry)
            count+=1
    print(itemCount)
    for i in range(0,4):
        print("items" +str(items[i].queue))
            
                
            


def getOperation(op , worry):
    totalWorry = 0
    if re.match("\+.*",op):
        if re.match(".*old",op):
            totalWorry = worry + worry
        else:
            value = int(re.findall("[1-9]+",op)[0])
            totalWorry = worry + value
    elif re.match("\*.*",op):
        if re.match(".*old",op):
            totalWorry = worry * worry
        else:
            value = int(re.findall("[1-9]+",op)[0])
            totalWorry = worry * value
    return totalWorry


            

                
                

if __name__ == "__main__":
    monkey()