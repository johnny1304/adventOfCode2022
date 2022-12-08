import queue
from copy import deepcopy


def tuning():
    with open("../resources/input.txt","r") as file:
        count=0
        q = queue.Queue(14)
        s = []
        for line in file:
            for char in line:
                count+=1
                if q.qsize()>13:
                    s.remove(q.get())
                q.put(char)
                s.append(char)
                print(q.qsize())
                if len(s)==14 and checkUnique(s):
                    print(s)
                    print(count)
                    break
                print(s)


def checkUnique(s):
    t = set()
    for i in s:
        t.add(i)
    return len(t)>13

if __name__=="__main__":
    tuning()