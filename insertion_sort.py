def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        temp = arr[i]

        while arr[j] > temp and j>=0:
            arr[j+1],arr[j] = arr[j],temp
            j -=1
    print(arr)

arr = [5,3,7,2,8,1]
insertion_sort(arr)
