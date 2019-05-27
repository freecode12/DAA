import time

import random



def partition(arr,low,high):

        i = low-1

        pivot = arr[high]

        for j in range(low,high):

                if arr[j] <= pivot:

                        i += 1

                        arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1

def quick_sort(arr,low,high):

        if low < high:

                pi = partition(arr,low,high)

                quick_sort(arr,low,pi-1)

                quick_sort(arr,pi,high)

m= int(input("enter the no. of elements in the list: "))

a=[random.randint(0,100) for i in range(0,m)]

print(a)

start = time.clock()

quick_sort(a,0,(len(a)-1))

end = time.clock()

print(a)

print (end-start)

