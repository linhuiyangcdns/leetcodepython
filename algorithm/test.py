from collections import deque

############ 初始化队列
x = deque([]) #x 代表横坐标
y = deque([]) #y 代表纵坐标
s = deque([]) #s 代表步长

#初始化迷宫最大值和标记数组
a = [[0 for col in range(50)] for row in range(50)]
book = [[0 for col in range(50)] for row in range(50)]

#初始化迷宫的四种走法
next_step = [[0, 1],  # 向右走
             [1, 0],  # 向下走
             [0, -1],  # 向左走
             [-1, 0]  # 向上走
             ]

#初始化起点和终点 以及迷宫数组
start_x = 0
start_y = 0
end_x = 3
end_y = 2
migong_array = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]

#将给定的迷宫填入a中
for i in range(len(migong_array)):
    for j in range(len(migong_array[0])):
        a[i][j] = migong_array[i][j]

#初始化队列的head 和tail
head = 0;tail = 0

x.append(start_x)
y.append(start_y)
s.append(0)
tail += 1

#将起点标记为1，代表已经走过
book[start_x][start_y] = 1

print('Initialize the x_queue:{}'.format(x))
print('Initialize the y_queue:{}'.format(y))
print('Initialize the s_queue:{}'.format(s))


flag = 0 #flag 是否达到终点，0表示没有，1表示达到
while (head < tail):
    for i in range(len(next_step)):
        next_x = x[head] + next_step[i][0]
        next_y = y[head] + next_step[i][1]

        if(next_x < 0 or next_y < 0 or next_x > len(migong_array) or next_y > len(migong_array[0])):
            continue
        if(a[next_x][next_y] == 0 and book[next_x][next_y] == 0):
            book[next_x][next_y] = 1   #标记之后不需要在重置，跟DFS不同，因为采用的是队列，每个点只入队列一次
            x.append(next_x) ; y.append(next_y) ; s.append(s[head] + 1)    #分别追加到queue，步长逐渐累加
            tail += 1
        if(next_x == end_x and next_y == end_y):
            flag = 1
            break
    if(flag == 1):
        break
    head += 1 #继续对后面的点进行扩展

print('The end of the x_queue:{}'.format(x))
print('The end of the y_queue:{}'.format(y))
print('The end of the s_queue:{}'.format(s))
print('The minimum of the path is: {0}'.format(s[tail-1]))