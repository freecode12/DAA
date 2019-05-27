#include<stdio.h>
int limit,mat[25][25],cost=0,visited[10];
int tsp(int c)
{
        int nearest=999,min=999,temp,count;
        for(count=0;count<limit;count++)
        {       if(mat[c][count]!=0&&visited[count]==0)
                {
                        if(mat[c][count]<min)
                        {       min=mat[count][0]+mat[c][count];}
                        temp=mat[c][count];
                        nearest=count;
                }
        }
        if (min!=999)
                cost+=temp;
        return nearest;
}
void mincost(int city)
{
        int nearest;
        printf("  %d",city+1);
        visited[city]=1;
        nearest=tsp(city);
        if(nearest==999)
        {
                nearest=0;
                printf("  %d",nearest+1);
                cost+=mat[city][nearest];
                return;
        }
        mincost(nearest);
}
int main()
{
        int i,j;
        printf("Enter the total number of cities:");
        scanf("%d",&limit);
        printf("\nEnter the cost matrix:\n");
        for(i=0;i<limit;i++)
        {
                printf("Enter row %d:",i+1);
                for(j=0;j<limit;j++)
                        scanf("%d",&mat[i][j]);
                visited[i]=0;
        }
        printf("\nThe entered cost matrix is:\n");
        for(i=0;i<limit;i++)
        {
                for(j=0;j<limit;j++)
                        printf("%d\t",mat[i][j]);
                printf("\n");
        }
        printf("\nPath-->");
        mincost(0);
        printf("\nMINIMUM COST IS: %d\n",cost);
        return 0;
}
