locations = []
knots = {"H":[0,0],"1":[0,0],"2":[0,0],"3":[0,0],"4":[0,0],"5":[0,0],"6":[0,0],"7":[0,0],"8":[0,0],"9":[0,0],}

def rope():
    with open("day9/resources/input.txt","r") as file:
        locations.append("0,0")
        for line in file:
            # print("move :"+line)
            instructions = line.strip("\n").split(" ")
            direction = instructions[0]
            distance = int(instructions[1])
            head=knots.get("H")
            if (direction == "U"):
                # print("distance :"+str(distance))
                for i in range(0,distance):
                    # print("loop")
                    head[1]+=1
                    calculateTail()
            elif (direction == "D"):
                for i in range(0,distance):
                    head[1]-=1
                    calculateTail()
            elif (direction == "R"):
                for i in range(0,distance):
                    head[0]+=1
                    calculateTail()
            elif (direction == "L"):
                for i in range(0,distance):
                    head[0]-=1
                    calculateTail()
    print(len(locations))
    print(locations)
    print(len(set(locations)))

def calculateTail():
    tail=[]
    head=[]
    for i in range(1,10):
        if(i==1):
            head=knots.get("H")
            tail=knots.get(str(i))
        else:
           head=knots.get(str(i-1))
           tail=knots.get(str(i)) 
        
        print("head: "+str(head)+ " Tail: "+str(tail))
        if(abs(tail[0] - head[0]) + abs(tail[1] - head[1]) >2):
            if(tail[0]<head[0]):
                tail[0]+=1
            elif(tail[0]>head[0]):
                tail[0]-=1
            if(tail[1]<head[1]):
                tail[1]+=1
            elif(tail[1]>head[1]):
                tail[1]-=1
        elif (abs(tail[0] - head[0])>1):
            if(tail[0]<head[0]):
                tail[0]+=1
            else:
                tail[0]-=1
        elif (abs(tail[1] - head[1])>1):
            if(tail[1]<head[1]):
                tail[1]+=1
            else:
                tail[1]-=1
        if(i == 9):
            locations.append(str(tail[0])+","+str(tail[1]))
    

if __name__=="__main__":
    rope()