import os
import time

maze = []
i,j = 8, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dz = ['북','동','남','서']

with open("/home/dongkyu/catkin_ws/src/level1.map", 'r', encoding='UTF-8') as f:
        while True:
                line = f.readline().split()
                maze.append(line)
                if not line:
                        break

def loadmap():
        maze_li = sum(maze, [])
        maze_str = ' '.join(maze_li)
        for l in range(1,10):
                print(maze_str[18*(l-1):18*l], end = '\n' )
        pass

if __name__ == "__main__":
        while (i != 0 or j != 8):
                dir = []
                cnt = 0 
                os.system('clear')
                loadmap()
                print(f'현재 플레이어: ([P] row:{i}, col:{j})')
                for x in range(0,4):     
                        try:
                                if ((maze[i+dx[x]][j+dy[x]] == 'o' or maze[i+dx[x]][j+dy[x]] == 'F' or maze[i+dx[x]][j+dy[x]] == 'S') and i+dx[x] >= 0 and j+dy[x] >= 0 and i+dx[x] < 9 and j+dy[x] < 9):
                                        cnt += 1
                                        print(f'{cnt}. {dz[x]}쪽로 가능')
                                        dir.append(dz[x])
                        except:
                                pass
                try:
                        a = int(input("어느방향으로 가실겁니까?(숫자로만) "))
                        b = a - 1
                        if dir[b] == '북':
                                maze[i][j], maze[i-1][j] = maze[i-1][j], maze[i][j]
                                i -= 1
                        elif dir[b] == '남':
                                maze[i][j], maze[i+1][j] = maze[i+1][j], maze[i][j]
                                i += 1
                        elif dir[b] == '서':
                                maze[i][j], maze[i][j-1] = maze[i][j-1], maze[i][j]
                                j -= 1
                        elif dir[b] == '동':
                                maze[i][j], maze[i][j+1] = maze[i][j+1], maze[i][j]
                                j += 1
                except:
                        print("잘못된 길입니다")
                        time.sleep(1)
                        pass    


                if (i != 8 or j != 0):
                        maze[8][0] = 'S'

                if (maze[7][0] == 'S'):
                        maze[7][0] = 'o'

        maze[0][7] = 'o'
        loadmap()
        print("도착했습니다!!!!!!!!!")