print("Enter the array:")
a=[int(x) for x in input().split()]
for i in range(len(a)):
        l=i
        for j in range(i+1,len(a)):
                if a[j]<a[l]:
                        l=j
        a[i],a[l]=a[l],a[i]
print("After sorting:",a)
