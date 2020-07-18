def findMinDiff(arr, n): 
    diff = 10**20
    for i in range(n-1): 
        for j in range(i+1,n): 
            if abs(arr[i]-arr[j]) < diff: 
                diff = abs(arr[i] - arr[j]) 
    return diff,arr[i],arr[j] 
a = [3,1,2,6,4]
print(findMinDiff(a,5)