import time

filename = ""
grid = []

def display():
    for j in range(len(grid)):
        row = ""

        for i in range(len(grid[0])):
            row += str(grid[i][j] + " ")
        print(row + "\n")

def graph(point):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nextPoint = (x + dx, y + dy)

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

def loop():
    pass

def search():
    pass

if __name__ ==  '__main__':
    import sys
    _, filename = sys.argv
    load()
