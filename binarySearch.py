sortedArray = [2,4,5,6,7,8,9,11,25,56,66]
search_num = int(input(f"enter a number to find index of {sortedArray} - "))

def binary_search(arr, item):
    left = 0
    right = len(arr) - 1
    
    while(left <= right):
        mid = (left + right) // 2
        if(arr[mid] == item):
            return mid
        elif(arr[mid] < item):
            left = mid + 1
        else:
            right = mid - 1
    return None

result = binary_search(sortedArray, search_num)
if result != None:
    print (f"Index of {search_num} is {result}")
else:
    print (f"Entered Number {search_num} is  not present in list")
