def find_peak(A):
    n = len(A)

    if n == 1:
        return 0

    j = n//2

    if (j == 0 and A[j] > A[j+1]) or (j == n and A[j] > A[j-1]) or (A[j-1] < A[j] and A[j] > A[j+1]):
        return j

    if A[j] < A[j-1]:
        return find_peak(A[0:j])
    else:
        return (j+1) + find_peak(A[j+1:])

A = [3,7,5,9,10,12,4,6,8,10,13,15,17,9,5,6,7,10,15,16,13,12,7,14,12,10,8,5,7,10,12,11]
print(find_peak(A))
print(A[find_peak(A)])