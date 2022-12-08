def findDuplicate():
    total=0
    with open("../resources/input.txt","r") as file:
        i=0
        lines = file.readlines()
        while i < len(lines):
            first = lines[i]
            second = lines[i+1]
            third = lines[i+2]
            i+=3
            for char in first:
                if char in second:
                    if char in third:
                        total+=getPriority(char)
                        break
    print(total)

def getPriority(x):
    if x.isupper():
        return ord(x.lower()) - 70
    else:
        return ord(x) - 96

if __name__== "__main__":
    findDuplicate()