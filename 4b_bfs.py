def inpu(g):
        print("Enter the edges or -1 to stop")
        while(1):
                x=[int(a) for a in input().split()]
                if x[0]==-1:
                        break
                if x[0] in g.keys():
                        g[x[0]].append(x[1])
                else:
                        g[x[0]]=[x[1]]
                if x[1] in g.keys():
                        g[x[1]].append(x[0])
                else:
                        g[x[1]]=[x[0]]
        print("Adjacency list ->",g)
def bfs(g,i):
        v={}
        for x in g.keys():
                v[x]=False
        L=[[i]]
        v[i]=True
        print("->",i,end=" ")
        level=0
        while(L[level]):
                L.append([])
                for n in g.keys():
                        for k in g[n]:
                                if not v[k]:
                                        L[level+1]=k
                                        v[k]=True
                                        print("->",k,end=" ")
                level+=1
g={}
inpu(g)
n=int(input("Enter the initial node for bfs:"))
bfs(g,n)
