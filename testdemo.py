def minOperations(arr, n):
 
    # Initializing vector of pair type which contains value
    # and index of arr
    vect = []
    for i in range(n):
        vect.append([arr[i], i])
 
    # Sorting array num on the basis of value
    vect.sort()
 
    # Initializing variables used to find maximum
    # length of increasing streak in index
    res = 1
    streak = 1
    prev = vect[0][1]
    for i in range(1,n):
        if (prev < vect[i][1]):
            res += 1
 
            # Updating streak
            streak = max(streak, res)
        else:
            res = 1
        prev = vect[i][1]
 
    # Returning number of elements left except streak
    return n - streak
 
# Driver code
arr = [ 4, 7, 2, 3, 9 ]
n = len(arr)
count = minOperations(arr, n)
print(count)