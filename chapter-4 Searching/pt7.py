# Count 1's in a sorted binary list

# 1 recursive solution
# def countOnes(arr,low,high):
#     if high >= low:
#         mid = low + (high-low)//2
#         if ((mid == high or arr[mid + 1]== 0) and (arr[mid] == 1)):
#             return mid + 1
#         if arr[mid] == 1:
#             return countOnes(arr,(mid+1),high)
#         return countOnes(arr,low,mid-1)
#     return 0
# arr = [1,1,1,1,0,0,0]
# print("Count of 1's in given array is",countOnes(arr,0,len(arr) - 1))
        
# 2 Binary Search Solution 

def countOnes(arr,n):
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low + high) // 2

        if (arr[mid] < 1):
            high = mid + 1
        else:

            if (mid == n - 1 or arr[mid + 1]!= 1):
                return mid + 1
            else:
                low = mid + 1
    return 0
if __name__ == '__main__':
    arr = [1,1,1,1,0,0,0]
    n = len(arr)
    print("Count of 1's in given array is",countOnes(arr,n))            