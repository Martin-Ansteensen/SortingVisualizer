import random
import copy
import time


data_size = 3000
#unsorted_array = random.sample(range(0, data_size), data_size)
unsorted_array = [4, 7, 6, 8, 0, 2, 3, 9, 5, 1]
#print(unsorted_array)

def bubble_sort(arr):
    start_time = time.time()
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print(arr) 
    print("--- %s seconds ---" % (time.time() - start_time))    
            

def insertion_sort_my(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        for j in range(1, i+1):            
            if arr[i-j+1] < arr[i-j]:
                arr[i-j+1], arr[i-j] = arr[i-j], arr[i-j+1]
            else:
                break
    print(arr)
    print("--- %s seconds ---" % (time.time() - start_time))

def insertion_sort_2(arr):
    start_time = time.time()
    for org_pos in range(1, len(arr)):
        curr_pos = org_pos
        
        while arr[curr_pos] < arr[curr_pos-1] and curr_pos > 0:
            arr[curr_pos], arr[curr_pos-1] = arr[curr_pos-1], arr[curr_pos]
            curr_pos -=1
    print("--- %s seconds ---" % (time.time() - start_time))
    #print(arr)

def insertion_sort(arr):
    start_time = time.time()
    for org_pos in range(1, len(arr)):
        curr_pos = org_pos
        org_val = arr[org_pos]
        while org_val > arr[curr_pos-1] and curr_pos > 0:
            arr[curr_pos] = arr[curr_pos-1]
            curr_pos -=1
        arr[curr_pos] = org_val
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(arr)


# From website
def insertionSort(alist):
    start_time = time.time()
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
        
    print("--- %s seconds ---" % (time.time() - start_time))


#bubble_sort(unsorted_array)
insertionSort(unsorted_array)
#insertion_sort(unsorted_array)


