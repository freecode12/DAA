import time

import random



def quick_sort(alist, start, end):

    if end - start > 1:

        p = partition(alist, start, end)

        quick_sort(alist, start, p)

        quick_sort(alist, p + 1, end)

def partition(alist, start, end):

    pivot = alist[start]

    i = start + 1

    j = end - 1



    while True:

        while (i <= j and alist[i] <= pivot):

            i = i + 1

        while (i <= j and alist[j] >= pivot):

            j = j - 1



        if i <= j:

            alist[i], alist[j] = alist[j], alist[i]

        else:

            alist[start], alist[j] = alist[j], alist[start]

            return j

print("enter an array")

alist = [random.randint(0,99) for x in range(10)]

print('Unsorted list: ', end='')

print(alist)

print('sorted list: ', end='')

start = time.clock()

quick_sort(alist,0,(len(alist)-1))

end = time.clock()

print(alist)

print (end-start)

