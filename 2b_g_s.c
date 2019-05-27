#include<stdio.h>
#define max 50
int men[max][max],women[max][max],mmark[max],wc[max],mc[max];
int wprefer(int w,int m,int m1,int n)
{
        int i;
        for(i=1;i<=n;i++)
        {

                if (women[w][i]==m)
                        return 1;
                else
                        if(women[w][i]==m1)
                                return 0;
        }
}
void stable(int n)
{
        int fc,i;
        for(i=1;i<=max;i++)
        {
                mmark[i]=0;
                wc[i]=-1;
        }
        fc=n;
        while(fc>0)
        {

                int m;
                for(m=1;m<=n;m++)
                        for(i=1;i<=n&&mmark[m]==0;i++)
                        {
                                int w=men[m][i];
                                if(wc[w]==-1)
                                {
                                        wc[w]=m;
                                        mmark[m]=1;
                                        fc--;
                                }
                                else
                                {
                                        int m1=wc[w];
                                        if(wprefer(w,m,m1,n))
                                        {
                                                wc[w]=m;
                                                mmark[m]=1;
                                                mmark[m1]=0;
                                        }
                                }
                        }
        }
}
int main()
{
int n,i,j;
printf("\nHow many men and women?:");
scanf("%d",&n);
printf("\nEnter the men preference:\n");
for(i=1;i<=n;i++)
{
        printf("Enter the preference of man %d:",i);
        for(j=1;j<=n;j++)
                scanf("%d",&men[i][j]);
}
printf("\nEnter the women preference:\n");
for(i=1;i<=n;i++)
{
        printf("Enter the preference of woman %d:",i);
        for(j=1;j<=n;j++)
                scanf("%d",&women[i][j]);
}
printf("\nMENS PREFERENCE LIST\n");
for(i=1;i<=n;i++)
{
        for(j=1;j<=n;j++)
                printf("%d    ",men[i][j]);
        printf("\n");
}
printf("\nWOMENS PREFERENCE LIST\n");
for(i=1;i<=n;i++)
{
        for(j=1;j<=n;j++)
                printf("%d    ",women[i][j]);
        printf("\n");
}
stable(n);
for(i=1;i<=n;i++)
        mc[wc[i]]=i;
printf("STABLE MATCHING DONE:\n");
for(i=1;i<=n;i++)
        printf("Woman %d is matched with man %d \n",i,mc[i]);
return 0;
}
