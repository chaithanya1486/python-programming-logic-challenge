def evenOdd(arr):
    # code here
    e= []
    o = []
    for i in range(len(arr)):
        if arr[i]%2==0:
            e.append(arr[i])
        else :
            o.append(arr[i])
    return e,o
