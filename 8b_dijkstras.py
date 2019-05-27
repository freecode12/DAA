def inpu():
        global graph,wt
        print("Enter the edges with weights,-1 to exit:")
        while 1:
                e=input().split()
                if e==['-1']:
                        break
                e[2]=int(e[2])
                if e[0]!=e[1]:
                        if e[0] in graph.keys():
                                if e[1] not in graph[e[0]]:
                                        graph[e[0]].append(e[1])
                        else:
                                graph[e[0]]=[e[1]]
                        if e[1] in graph.keys():
                                if e[0] not in graph[e[1]]:
                                        graph[e[1]].append(e[0])
                        else:
                                graph[e[1]]=[e[0]]
                        if (e[0],e[1]) in wt.keys():
                                wt[e[0],e[1]]=wt[e[1],e[0]]=min(e[2],wt[e[0],e[1]])
                        else:
                                wt[e[0],e[1]]=wt[e[1],e[0]]=e[2]
def dijuk(s):
        global graph
        path={}
        dist={}
        visited={}
        for x in graph.keys():
                (visited[x],path[x])=(False,[])
        path[s]=[s]
        visited[s]=True
        marked=[s]
        for x in graph.keys():
                dist[x]=[float('inf')]
        dist[s][0]=0
        i=1
        while i<len(graph.keys()):
                u=marked[i-1]
                mini=float('inf')
                nxt=''
                for j in graph.keys():
                        dist[j].append(dist[j][i-1])
                for j in graph[u]:
                        if not visited[j] and dist[u][i]+wt[u,j]<dist[j][i-1]:
                                dist[j][i]=dist[u][i]+wt[u,j]
                                path[j]=path[u]+[j]
                for j in graph[u]:
                        if not visited[j]:
                                if dist[j][i]<mini:
                                #       path[j]=path[u]+[j]
                                        mini=dist[j][i]
                                        nxt=j
                marked.append(nxt)
                visited[nxt]=True
                i+=1
        return (path,dist)
graph={}
wt={}
inpu()
s=input("Enter the source node:")
(path,dist)=dijuk(s)
print("------------------SHORTEST PATH-------------------\n")
for i in sorted(graph.keys()):
        print("Vertex ",i)
        for j in path[i][:-1]:
                print(j,"---->",end=" ")
        print(path[i][-1],"\nWeight = ",dist[i][-1],end="\n\n")
