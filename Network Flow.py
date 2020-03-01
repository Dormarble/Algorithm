import queue

INF = 1000000000
nodeNum = 6
c = []
f = []
for i in range(nodeNum+1):
    c.append([0]*(nodeNum+1))
    f.append([0]*(nodeNum+1))
d = [-1]*(nodeNum+1)
a = [[] for _ in range(nodeNum+1)]

def maxFlow(start, end) :
    result = 0
    while True:
        d = [-1]*(nodeNum+1)
        q = queue.Queue()
        q.put(start)
        while(not(q.empty())):
            x = q.get()

            for y in a[x]:
                if c[x][y] - f[x][y] > 0 and d[y] == -1 :
                    q.put(y)
                    d[y] = x
                    if y == end :
                        break
        if d[end] == -1:
            break
        flow = INF
        i = end
        while i!=start :
            flow = min(flow, c[d[i]][i] - f[d[i]][i])
            i = d[i]
        i = end
        while i!=start :
            f[d[i]][i] = f[d[i]][i] + flow
            f[i][d[i]] = f[i][d[i]] - flow
            i = d[i]
        result += flow
    
    return result

a[1].append(2)
a[2].append(1)
c[1][2] = 12
   
a[1].append(4)
a[4].append(1)
c[1][4] = 11
    
a[2].append(3)
a[3].append(2)
c[2][3] = 6
    
a[2].append(4)
a[4].append(2)
c[2][4] = 3
    
a[2].append(5)
a[5].append(2)
c[2][5] = 5
    
a[2].append(6)
a[6].append(2)
c[2][6] = 9

a[3].append(6)
a[6].append(3)
c[3][6] = 8
    
a[4].append(5)
a[5].append(4)
c[4][5] = 9
    
a[5].append(3)
a[3].append(5)
c[5][3] = 3
    
a[5].append(6)
a[6].append(5)
c[5][6] = 4


print(maxFlow(1, 6))