def largest(arr,n):
    #initalise maximun element
    max=arr[0]
    for i in range(1,n):
        if(arr[i]>max):
            max=arr[i]
    return max
def smallest(arr,n):
    min=arr[0]
    for i in range(1,n):
        if(arr[i]<min):
            min=arr[i]
    return min
print("these are the time from stopwatches in seconds")
arr=[2,6,10,42,3]
n=len(arr)

a=largest(arr,n)
b=smallest(arr,n)
print("largest in the given array is:",a)
print("smallest in the given array is:",b)




