def bell(li,n,s):
        dist=[999 for i in range(n+1)]
        path=[[None] for i in range(n+1)]
        path[s]=[s]
        dist[s]=0
        for i in range(n-1):
                for pair in li:
                        temp=dist[pair[1]]
                        dist[pair[1]]=min(dist[pair[1]],dist[pair[0]]+pair[2])
                        if temp!=dist[pair[1]]:
                                path[pair[1]]=path[pair[0]]+[pair[1]]
        del(dist[0])
        del(path[0])
        print(dist)
        print("Distance from the source:\n")
        j=0
        for i in dist:
                print("Node ",j,":Cost ",i,"\n")
                j+=1
        for i in path:
                print(s,"--->",path.index(i)+1,":",i)
li=[]
n=int(input("How many nodes?:"))
e=int(input("How many edges?:"))
for i in range(e):
        print("\nNEXT EDGE")
        u=int(input("Enter u:"))
        v=int(input("Enter v:"))
        w=int(input("Enter the weight:"))
        l=[u,v,w]
        li.append(l)
s=int(input("\nEnter the source:"))
bell(li,n,s)
