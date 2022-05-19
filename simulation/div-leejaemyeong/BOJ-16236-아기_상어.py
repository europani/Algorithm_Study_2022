import sys
from collections import deque

N=int(input())
arr=[]

shark_x,shark_y=0,0 # ����� ��ġ
shark_size=2 # ����� ũ��
eat_cnt=0 # �� ���� ����� ��
fish_cnt=0 # ����� ��
time=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        # ����� ��ǥ ����
        if arr[i][j]==9:
            shark_x,shark_y=i,j
            arr[i][j]=0
        #������� ���� ī����
        elif 0<arr[i][j]<=6:
            fish_cnt+=1

def BFS(shark_x,shark_y):
    vis = [[False for _ in range(N)] for _ in range(N)]
    deq=deque()
    deq.append([shark_x,shark_y,0])
    vis[shark_x][shark_y]=True
    #���� �� �ִ� ���������� �ִܰŸ� ������ ����
    min_dis=sys.maxsize
    #������� ��ǥ�� �Ÿ� ����
    fish_list=[]
    while deq:
        x,y,dis=deq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and not vis[nx][ny]:
                #�̵��� ���� shark_size���� �۰ų� ������ �̵��� �� �����Ƿ�
                #�ش� ��ǥ�� vis�迭 True�� ����
                if arr[nx][ny]<=shark_size:
                    vis[nx][ny]=True
                    #�̵��� ���� 0���� ũ�� shark_size���� ������ ���� �� �ִ�
                    #������̹Ƿ� min_dis�� �̵��Ÿ� ����
                    if 0<arr[nx][ny]<shark_size:
                        #�̵��Ÿ��� min_dis���� ũ�� �ִܰŸ��� �ƴϱ� ������ pass
                        if min_dis>=dis+1:
                            min_dis=dis+1
                            #�ִܰŸ��� ����� ��ǥ, �Ÿ� ����
                            fish_list.append((nx,ny,dis+1))
                    #�̵��� ��ǥ�� ���� 0�̰� �̵��Ÿ��� min_dis���� ������ ����
                    #���� �� �ִ� ����⸦ ã�� ���߱� ������ deq�� �ش� ��ǥ,�Ÿ� ����
                    if dis+1<min_dis:
                        deq.append([nx,ny,dis+1])
    #���� fish_list�� �����Ͱ� ��������� �ִܰŸ��� ���� �� �ִ�
    #����⸦ ã�ұ� ������ �ش� �迭�� �������� �������ش�.
    #(�������� �����ϸ� x��ǥ�� ���� ��, ���� ������ y��ǥ�� ���������� �����)
    #�̶� �̵��Ÿ��� ��� �ִܰŸ��� ����Ǿ� ���� ���Ŀ� ������ ��ġ�� ����
    if fish_list:
        fish_list.sort()
        print(fish_list)
        #���� ���� �ְ� ���� ���ʿ� �ִ� �ִܰŸ��� ���� �� �ִ� ����⸦ ��ȯ
        return fish_list[0]
    else:
        return False



while fish_cnt:
    result=BFS(shark_x,shark_y)
    if not result:
        break
    shark_x,shark_y=result[0],result[1]
    time+=result[2]
    eat_cnt+=1
    fish_cnt-=1
    if shark_size==eat_cnt:
        shark_size+=1
        eat_cnt=0
    arr[shark_x][shark_y]=0

print(time)

