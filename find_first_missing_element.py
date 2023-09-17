##################################################
##  Problem 4.d Oh, mamma mia!
##################################################

# Given a list of positive integers and the starting integer s, return x such that x is the smallest value greater than
# or equal to s that's not present in the list

def find_first_missing_element(arr, s):
    '''
    Inputs:
        arr        (list(int)) | List of sorted, unique positive integer order id's
        s          (int)       | Positive integer
    Output:
        -          (int)       | The smallest integer greater than or equal to s that's not present in arr
    '''

    pos = find(arr, s)

    if pos == -1: #s does not exist in array
        return s
    else:
        ind = find_non_consec(arr, pos)
        return arr[ind-1]+1
        # may still have some edge cases here idk maybe formalize later lmao

    pass

def find(arr, s):
    '''
        Inputs:
            arr        (list(int)) | List of sorted, unique positive integer order id's
            s          (int)       | Positive integer
        Output:
            -          (int)       | position of s in arr if s exists, else -1
        '''

    l = 0
    r = len(arr)

    while l != r:
        mid = l + (r-l)//2
        if arr[mid] == s:
            return mid

        if arr[mid] > s:
            r = mid
        else:
            l = mid + 1

    return -1

def find_non_consec(arr, pos):
    '''
        Inputs:
            arr        (list(int)) | List of sorted, unique positive integer order id's
            pos         (int)      | position of s
        Output:
            -          (int)       | position of last element of consecutive segment starting from s
    '''
    l = pos
    r = len(arr)

    while l != r:
        mid = l + (r-l)//2

        if(arr[mid] - arr[pos]) > (mid - pos): #section is consecutive
            r = mid
        else:
            l = mid + 1

    return l

#print(find_first_missing_element([3, 5, 6, 7, 10, 11], 8))
#print(find_first_missing_element([1, 2, 3, 4, 5, 6], 4))
#print(find_first_missing_element([2, 3, 4, 5, 6], 1))
#print(find_first_missing_element([2, 3, 4, 5, 6, 8], 3))