import queue
import re

def monkey():
    items = [queue.Queue()]*8
    operations = [""]*8
    tests = [0]*8
    trueAction = [0]*8
    falseAction = [0]*8
    count=-1
    with open("day11/resources/input.txt","r") as file:
        for line in file:
            if re.match("Monkey "+str(count+1)+":.*",line):
                print(line)
                count+=1
            elif re.match(".*Starting items:.*",line):
                for item in re.findall("[0-9]+",line):
                    items[count].put(item)
            elif re.match(".*Operation:.*",line):
                words = line.strip("\n").split(" ")
                operations[count]=words[-2]+words[-1]
            
                
            


            
            

                
                

if __name__ == "__main__":
    monkey()