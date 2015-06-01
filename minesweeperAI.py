import time
from heapq import heappush, heappop

filename = ""
grid = []

def method():
    count =0
    tempTurnToflag ={}
    turnToflag = {}
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            count =0
            tempTurnToflag ={}
            for num in range(1,8):
                if grid[i][j] == str(num):
                    #print adj(i,j)
                    adjBox = adj(i,j)
                    for element in adjBox:

                        #print element
                        if adjBox[element] == "W" or adjBox[element]=="F":
                            count += 1
                            tempTurnToflag[element] = "F"
                    if count == num:
                        #print tempTurnToflag
                        #z always equal to none
                        z = turnToflag.update(tempTurnToflag)
    print turnToflag
    f = open('out.txt', 'w')
    print >> f, turnToflag
    f.close()

def methodProbability():
    count =0
    disElement = []
    elementValue = {}

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            for num in range(1,8):
                if grid[i][j] == str(num):
                    adjBox = adj(i,j)
                    for element in adjBox:
                        if adjBox[element] == 'W':
                            if element not in disElement:
                                elementValue[element] = num
                                disElement.append(element)
                            else:
                                elementValue[element] = elementValue[element] + num

    print elementValue
    f = open('outPribability.txt', 'w') 
    for value in range(1,9):        
        for choice in elementValue:
            if count <=2:
                if elementValue[choice] == value:
                    print choice
                                                       
                    print >> f, choice
                    count +=1
    f.close()





def methodMatrices():
    dicUnclickedTiles= {}
    unclickedTiles = []
    equation = {}

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            unclickedTiles = []
            equation = {}
            for num in range(1,8):
                if grid[i][j] == str(num):
                    adjBox = adj(i,j)
                    for element in adjBox:
                        if adjBox[element] == "W":
                            heappush(unclickedTiles, element)
                            dicUnclickedTiles[element] = 'W'
                    
                    equation[num] = unclickedTiles
                    #print equation
    print dicUnclickedTiles
    for wall in dicUnclickedTiles:
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                unclickedTiles = []
                equation = {}
                for num in range(1,8):
                    if grid[i][j] == str(num):
                        adjBox = adj(i,j)
                        for element in adjBox:
                            if adjBox[element] == "W":
                                heappush(unclickedTiles, element)                   
                        equation[num] = unclickedTiles
                        for tiles in equation[num]:
                            if tiles == wall:
                                print equation
        print






def display():
    for j in range(len(grid)):
        row = ""

        for i in range(len(grid[0])):
            row += str(grid[i][j] + " ")
        print(row + "\n")
    #print grid

def adj(x,y):
    nextBox={}
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (x+dx >= 0 and y+dy >= 0):
                nextBox[(x+dx,y+dy)]=grid[x+dx][y+dy]
    return nextBox
            

#def graph(point):
#   for dx in [-1, 0, 1]:
#      for dy in [-1, 0, 1]:
#         nextPoint = (x + dx, y + dy)

def load():
    file = open(filename, "r")
    mapHeight = int(file.readline())
    mapWidth = int(file.readline())
    grid[:] = []

    for i in range(mapHeight):
        grid.append([])

        for j in range(mapWidth):
            grid[i].append("Z")

    x = 0
    y = 0

    for j, line in enumerate(file.readlines()):
        x = 0

        for i, char in enumerate(line):
            if char == "\n" or char == "\r" or char == " ":
                continue
            elif char == "@":
                grid[x][y] = "W"
            else:
                grid[x][y] = char
            #print(str(x)+","+str(y))

            x += 1
        y += 1

    display()
    method()
    methodProbability()
    #methodMatrices()

def loop():
    pass

def search():
    pass

if __name__ ==  '__main__':
    import sys
    _, filename = sys.argv
    load()
