import re
import pandas as pd

def treeHouse():
    df = pd.read_csv("day8/resources/comma.csv",sep=",",header=None).T
    checkView(df)
    # with open("day8/resources/comma.csv","w") as file1:
    #     with open("day8/resources/input.txt","r") as file:
    #         for line in file:
    #             file1.writelines(re.sub(r'([0-9])(?!$)', r'\1,',line ))

def checkVisible(df):
    columnCount = 0
    for column in df:
        columnList = df[column].to_list()
        for i in range(0,len(columnList)):
            if column==0 or column==len(df)-1:
                columnCount+=1
            elif i == 0 or i==len(columnList)-1:
                columnCount+=1
            else:
                firstHalf = columnList[:i]
                secondHalf = columnList[i+1:]
                if len(firstHalf)==0 or len(secondHalf)==0 or max(firstHalf)<columnList[i] or max(secondHalf)<columnList[i]:
                    columnCount+=1
                else:
                    row = df.loc[i].to_list()
                    firstHalfRow = row[:column]
                    secondHalfRow = row[column+1:]
                    if len(firstHalfRow)==0 or len(secondHalfRow)==0 or max(firstHalfRow)<row[column] or max(secondHalfRow)<row[column]:
                        columnCount+=1
    print(columnCount)                
    return columnCount

def checkView(df):
    maxScenic = 0
    for column in df:
        columnList = df[column].to_list()
        print(columnList)
        for i in range(0,len(columnList)):
            left=0
            right=0
            up=0
            down=0

            current = columnList[i]
            print("Current: "+str(current))
            leftHalf = columnList[:i]
            leftHalf.reverse()
            print("leftHalf" + str(leftHalf))
            if len(leftHalf)>0:
                for tree in leftHalf:
                    if tree<current:
                        left+=1
                    else:
                        left+=1
                        break
                    

            rightHalf = columnList[i+1:]
            print("rightHalf" + str(rightHalf))
            if len(rightHalf)>0:
                for tree in rightHalf:
                    if tree<current:
                        right+=1
                    else:
                        right+=1
                        break
                   

            row = df.loc[i].to_list()
            # print("row:"+ str(row))
            upHalf=row[:column]
            upHalf.reverse()
            # print("UpHalf: "+str(upHalf))
            if len(upHalf)>0:
                for tree in upHalf:
                    if tree<current:
                        up+=1
                    else:
                        up+=1
                        break
                    
            downHalf=row[column+1:]
            # print("downHalf: "+str(downHalf))
            if len(downHalf)>0:
                for tree in downHalf:
                    if tree<current:
                        down+=1
                    else:
                        down+=1
                        break
                   
            print("down:"+str(down) + " up:"+str(up)+" right:"+str(right)+" left:"+str(left))
            score = up * down * right * left
            # print(score)
            if score>maxScenic:
                maxScenic = score
    print(maxScenic)



if __name__=="__main__":
    treeHouse()