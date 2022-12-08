import queue


def directorySpace():
    q = queue.LifoQueue()
    s = []
    dict = {}
    with open("../resources/input.txt","r") as file:
        for line in file:
            l = line.strip("\n").split(" ")
            if l[0] == "dir":
                continue
            elif(l[0] == "$"):
                if l[1] == "ls":
                    continue
                elif l[1] == "cd":
                    if l[2] == "..":
                        s.remove(q.get())
                        print(s)
                    else:
                        q.put(l[2])
                        s.append(l[2])
            else:

                for i in s:

                    if dict.__contains__(i):
                        dict[i] += int(l[0])
                    else:
                        dict[i] = int(l[0])
    availableSpace = 70000000 - max(dict.values())
    neededSpace = 30000000-availableSpace
    for i in dict.values():
        if i >=neededSpace:
            print(i)
if __name__=="__main__":
    directorySpace()