##################################################
##  Problem 3.c. Find the Missing Number 2
##################################################

# Given n integers in the range [0,N] where n <= N, find an integer
# in the range [0,N] that is missing. If there are multiple missing numbers,
# return any of them. There is at least one number in the range that is missing.
def find_missing_int(arr, N):
    '''
    Inputs:
        arr     (list(int)) | List of unsorted, unique positive integer order id's
        N       (int)       | A positive integer larger than len(arr)
    Output:
        -       (int)       | An integer in the range [0,N] not present in arr
    '''

    n = len(arr)
    mid = (n+1)//2
    small = arrange(arr, mid) #number of elements < n/2

    if small == n:
        return n

    if small == 0:
        return 0

    if small >= mid:
        for i in range(small, n):
            if arr[i] - mid < small:
                arr[arr[i] - mid] = -1

        for i in range(0, small):
            if arr[i] != -1:
                return mid + i
    else:
        for i in range(0, small):
            if arr[i] + small < n:
                arr[arr[i] + small] = -1

        for i in range(small, n):
            if arr[i] != -1:
                return i-small


def arrange(arr, m):
    small = 0
    n = len(arr)

    for i in range(0, len(arr)):
        if arr[i] < m:
            small += 1

    l = 0
    r = n-1

    while (l < small) and (r >= small):

        if (arr[l] >= m) and (arr[r] < m):
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp

        if arr[l] < m: #don't need to be swapped
            l += 1

        if arr[r] >= m: #don't need to be swapped
            r -= 1

    return small


#print(find_missing_int([0,1,3,4],4))
#print(find_missing_int([6,2,4,5,0,1,3],7))
#print(find_missing_int([6,8,3,2],8))