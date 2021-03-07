# Sorting of array without using inbuilt function i.e. sort()
#	without using function

# sorted Array using own defined function

arr = [91, 7, 52, 12, 76]
temp = 0

def sortArr(arr):
    print("The original Array is ")
    for i in range(0,len(arr)):
        print(arr[i],end=" ")


    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print("\n")

    print("The Sorted Array is :")
    for i in range(0,len(arr)):
        print(arr[i],end=" ")

sortArr(arr)