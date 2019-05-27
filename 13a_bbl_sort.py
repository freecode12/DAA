print("Enter the array:")
a=[int(x) for x in input().split()]
n=len(a)
for i in range(n):
        for j in range(n-i-1):
                if a[j]>a[j+1]:
                        a[j],a[j+1]=a[j+1],a[j]
print("After sorting:",a)
