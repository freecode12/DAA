import time

def bin(arr,l,r,x):
        if r>=l:
                mid= l + (r-1)//2
                if arr[mid]==x:
                        return mid
                elif x<arr[mid]:
                        return bin(arr,l,mid-1,x)
                else:return bin(arr,mid+1,r,x)
        else:return -1

print("Enter the array in any order:")
arr=[int(x) for x in input().split()]

print("Sorting the array using selection sort...")

m=time.clock()

for i in range(len(arr)-1):
        l=i
        for k in range(i+1,len(arr)):
                if arr[k]<arr[l]:
                        l=k
        (arr[l],arr[i])=(arr[i],arr[l])

print("The sorted array is:")
for i in arr:
        print(i,end=" ")
print()

x=int(input("Enter the element to be searched:"))
a=bin(arr,0,len(arr)-1,x)
n=time.clock()
if a!=-1:
        print(x," found at position ",a+1)
else:print("Not found")
print("TIME TAKEN:",(n-m),"s")
