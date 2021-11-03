def binary_search(arr, x):
    start = 0
    end = len(arr)
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    print(start)

binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13], 6)


    