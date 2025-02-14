
# Binary Search
# Time Complexity of Function 
# Best case  :- O(1)
# Avg Case   :- O(log(n))
# Worst Case : O(log(n))


def Binary_Search(arr, key, l, r):
    while(l<=r):
        mid = (l+r)//2 
        if arr[mid]==key:
            return "Key Found"
        elif key>arr[mid]:
            l = mid+1 
        elif key<arr[mid]:
            r = mid-1
        
    return "Key Not Found"
    
    
    
arr = list(map(int,input().split()))
key = int(input())

arr.sort()
print(Binary_Search(arr, key,0,len(arr)-1))