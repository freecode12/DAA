import heapq as hq

def Dijk(graph,start):

        n = len(graph)

        Q = [[0, start]]

        #print(Q)

        d = [999 for i in range(n)]

        #print(d)

        d[start]=0

        while Q:

                [length, u] = hq.heappop(Q)

                for v in range(n):

                        if d[v] > d[u] + graph[u][v]:

                                d[v] = d[u] + graph[u][v]

                                hq.heappush(Q, [d[v], v])

        return d

#graph = [[0, 5, 10, 999], [5, 0 ,4, 11],[10, 4, 0, 5], [999, 11, 5,0]]



graph = []

n = int(input("Enter number of nodes"))

print("Enter the weights of respective edges")

for i in range(0,n):

        m= []

        print( "Next edge . . .")

        for k in range(0,n):

                print( "From ", i+1 ," To ", k+1)

                val= int(input())

                m.append(val)

        graph.append(m)

        d = Dijk(graph,0)

        print (d)
