import time
print("Enter the array")
a=[int(x) for x in input().split()]
n=time.clock()
for i in range(1,len(a)):
        r=a[i]
        j=i-1
        while j>=0 and a[j]>r:
                a[j+1]=a[j]
                j-=1
        a[j+1]=r
m=time.clock()
print("The sorted array is:")
for i in a:
        print(i,end=" ")
print()
print("The time taken is:",m-n)
