def insort(a):
        for i in range(1,len(a)):
                r=a[i]
                j=i-1
                while j>=0 and a[j]>r:
                        a[j+1]=a[j]
                        j-=1
                a[j+1]=r
        return a
def bucket(x):
        arr=[]
        for i in range(10):
                arr.append([])
        for j in x:
                index=int(10*j)
                arr[index].append(j)
        for i in range(10):
                arr[i]=insort(arr[i])
        k=0
        for i in range(10):
                for j in range(len(arr[i])):
                        x[k]=arr[i][j]
                        k+=1
        return x
print("Enter the elements which are <1")
x = [float(x) for x in input().split()]
print("Sorted Array is")
print(bucket(x))
