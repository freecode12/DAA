def dfs(g,i):
        global visited
        visited[i]=True
        print("->",i,end=" ")
        for x in g[i]:
                if not visited[x]:
                        dfs(g,x)
g={}

print("Enter the edges and -1 to stop")
while(1):
    a=[int(x) for x in input().split()]
    if a[0] == -1:
        break
    if a[0] in g.keys():
        g[a[0]].append(a[1])
    else:
        g[a[0]]=[a[1]]
    if a[1] in g.keys():
        g[a[1]].append(a[0])
    else:
        g[a[1]]=[a[0]]

visited={}
for i in g.keys():
        visited[i]=False
n=int(input("Enter the starting node for DFS:"))
dfs(g,n)
