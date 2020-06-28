import time

map = [[1,3,0,0,0,1],
       [1,1,1,1,0,1],
       [1,0,0,0,0,1],
       [1,1,1,1,0,1],
       [1,0,0,0,0,1],
       [1,1,1,2,1,1]]

stack =[]
now = 2
nowPosition =[5,3]
#left = (n, k-1)
#right = (n, k+1)
#up = (n-1, k)
#down = (n+1, k)
for i in range(0,6):
    print(str(map[i]) + '\n')

print(map[5][3])

def leftPos(position):
    position[1] = position[1]-1
    if(position[1] < 0 or position[1] > 5):
        return 1
    row = position[0]
    col = position[1]
    position[1] = position[1] + 1
    blocked = map[row][col]
    return blocked

def rightPos(position):
    position[1] = position[1]+1
    if (position[1] < 0 or position[1] > 5):
        return 1
    row = position[0]
    col = position[1]
    position[1] = position[1] - 1
    blocked = map[row][col]
    return blocked

def upPos(position):
    position[0] = position[0]-1
    if (position[0] < 0 or position[0] > 5):
        return 1
    row = position[0]
    col = position[1]
    position[0] = position[0] + 1
    blocked = map[row][col]
    return blocked

def downPos(position):
    position[0] = position[0]+1
    if (position[0] < 0 or position[0] > 5):
        return 1
    row = position[0]
    col = position[1]
    position[0] = position[0] - 1
    blocked = map[row][col]
    return blocked

while now!=3:
    for i in range(0,6):
        print(str(map[i]) + '\n')
    now = leftPos(nowPosition)
    if(now != 1 and now != 4):
        print('left')
        nowPosition[1] = nowPosition[1] - 1
        map[nowPosition[0]][nowPosition[1]] = 4
        tmp = [nowPosition[0], nowPosition[1]]
        stack.append(tmp)
        continue

    now = rightPos(nowPosition)
    if (now != 1 and now != 4):
        print('right')
        nowPosition[1] = nowPosition[1] + 1
        map[nowPosition[0]][nowPosition[1]] = 4
        tmp = [nowPosition[0], nowPosition[1]]
        stack.append(tmp)
        continue

    now = upPos(nowPosition)
    if (now != 1 and now != 4):
        print('up')
        nowPosition[0] = nowPosition[0] - 1
        map[nowPosition[0]][nowPosition[1]] = 4
        tmp = [nowPosition[0], nowPosition[1]]
        stack.append(tmp)
        continue

    now = downPos(nowPosition)
    if (now != 1 and now != 4):
        print('down')
        nowPosition[0] = nowPosition[0] + 1
        map[nowPosition[0]][nowPosition[1]] = 4
        tmp = [nowPosition[0], nowPosition[1]]
        stack.append(tmp)
        continue

    if(len(stack) == 0):
        print('no exit')
        break
    nowPosition = stack.pop()


while len(stack) != 0:
    tmp = stack.pop()
    map[tmp[0]][tmp[1]] = 3

for i in range(0,6):
    print(str(map[i]) + '\n')


