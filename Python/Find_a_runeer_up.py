if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    for j in range(len(arr)):
        arr[j]=int(arr[j])
    arr.sort()
    for i in range(0,n):
        if arr[n-i-1]<arr[n-1]:
            print(arr[n-i-1])
            break
                          
                
                