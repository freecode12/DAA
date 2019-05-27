#include<stdio.h>

 int n,cost[10][10];

void kruskal();

int main()

{

int i,j;

// Read the number of nodes

printf("Enter the number of nodes\n"); scanf("%d",&n);

printf("Enter the cost matrix\n");

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

{

printf("Enter the cost between %d and %d\n",i,j);

scanf("%d",&cost[i][j]);

} }

kruskal();

return 0;

}

void kruskal() {

int i,parent[10],j,ne=0,mincost=0,u,v,min,a,b;

//Initialize the parent array.

for(i=1;i<=n;i++)

parent[i]=0;

//Algorithm : Unless n-1 edges

while(ne != n-1)

{min=999; // Get the min from the cost matrix

for(i=1;i<=n;i++)

{

for(j=1;j<=n;j++)

{

if(cost[i][j]<min)

{

min=cost[i][j];

a=u=i;

b=v=j;

}

}

} //Find the parent of each 'u' and 'v'.

while(parent[u]!=0)

u=parent[u];

while(parent[v]!=0)

v=parent[v];

if(u!=v)

{

 printf("The next node from %d-------> is %d with cost %d\n",a,b,min);

parent[v]=u;

ne=ne+1;

mincost=mincost+min;

}//Mark cost of 'a' and 'b' to infinity.

cost[a][b]=cost[b][a]=999;

}// end while

printf("The mincost is %d\n",mincost); }
