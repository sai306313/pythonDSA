#Linear Search
#Time Complexity of Function
#Best Case : O(1)
#Avg Case : O(N)
#Worst Case : O(N)

def Linear_Search(arr, key):
    
    for i in range(len(arr)):
        if arr[i] == key:
            return "key Found"
    
    return "key Not Found"
    
arr = list(map(int,input().split()))
key = int(input())

print(Linear_Search(arr, key))