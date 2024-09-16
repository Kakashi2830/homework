def second_smallest(arr):
    min=arr[0]
    seond_smallest=arr[len(arr)-1]
    for i in range(len(arr)):
        if arr[i]<=min:
            min=arr[i]
        elif arr[i]<seond_smallest and arr[i]!=min:
            seond_smallest=arr[i]
    return seond_smallest

arr=[1,7,6,3,8,3,5]
print(second_smallest(arr))