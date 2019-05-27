m=[]
schedule=[]
def find_pred(jobs,n):
        p=[0 for i in range(n+1)]
        cur=n
        chosen=cur-1
        while cur>1:
                if chosen<=0:
                        p[cur]=0
                        cur=cur-1
                        chosen=cur-1
                else:
                        if jobs[cur][0]<jobs[chosen][1]:
                                chosen=chosen-1
                        else:
                                p[cur]=chosen
                                cur=cur-1
                                chosen=cur-1
        return p
def opt(j,jobs,p):
        if j==0:
                return m[j]
        elif j==1:
                m[j]=max(jobs[j][2],0)
                return m[j]
        else:
                if m[j]==-1:
                        m[j]=max(opt(j-1,jobs,p),jobs[j][2]+opt(p[j],jobs,p))
                return m[j]
def wis(jobs,n):
        p=find_pred(jobs,n)
        value=opt(n,jobs,p)
        return value,p
def find(j,jobs,p):
        global m
        global schedule
        if j>0:
                if jobs[j][2]+m[p[j]]>=m[j-1]:
                        schedule.append(j)
                        find(p[j],jobs,p)
                else:
                        find(j-1,jobs,p)
        return
n=int(input("How many jobs?:"))
m=[-1 for i in range(n+1)]
jobs=[0]
m[0]=0
for i in range(n):
        print("\nFor job ",i+1,":")
        s=int(input("Enter start time:"))
        f=int(input("Enter finish time:"))
        v=int(input("Enter the weight:"))
        jobs.append((s,f,v))
max_value,p=wis(jobs,n)
print(m)
print("MAXIMUM VALUE IS:",max_value)
find(n,jobs,p)
print("The jobs are:",schedule)
