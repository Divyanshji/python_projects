def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr =[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5,1,55,12,9,33]))

# list1 = [55,6,88,54,0,2]
# list1.sort()
# print (list1)

# import sys
# sys.setrecursionlimit(1500)
# def countdown(i):
#     print(i)
#     if(i <=0 ):
#         # print (i)
#         return
#     else:
#         countdown (i- 1)
#         # return

# num = int(input("enter a number - "))
# result = countdown(num)