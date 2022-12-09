import pandas as pd

def treeHouse():
    df = pd.read_csv("../resources/input.txt", sep="", header=None)
    print(df)


if __name__=="__main__":
    treeHouse()