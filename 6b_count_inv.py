def merge(a):
        global inv
        if len(a)>1:
                print("Splitting ",a,"...")
                m=len(a)//2
                left=a[:m]
                right=a[m:]
                merge(left)
                merge(right)
                i=0
                j=0
                k=0
                while i<len(left) and j<len(right):
                        if left[i]<right[j]:
                                a[k]=left[i]
                                i+=1
                        else:
                                a[k]=right[j]
                                j+=1
                                inv+=len(left[i:])
                        k+=1
                while i<len(left):
                        a[k]=left[i]
                        i+=1
                        k+=1
                while j<len(right):
                        a[k]=right[j]
                        j+=1
                        k+=1
        print("Merging ",a,"...")
inv=0
print("Enter the array")
a=[int(x) for x in input().split()]
merge(a)
print("After merging",a)
print("Inversions:",inv)
