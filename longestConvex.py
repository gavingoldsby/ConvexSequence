import itertools
import time

def isConvex(A):
    isitConvex = True
    for x in range(1, len(A)-1):
        if A[x+1] - A[x] > A[x] - A[x-1]:
            isitConvex = True
        else:
            return False
    return isitConvex
def solve (A):
    n = len(A)
    s = [[0 for x in range(n)] for y in range(n)]
    s2 = [[0 for x in range(n)] for y in range(n)]
    
    for i in range (1, n):
        for j in range(0, n) :
            if i < 2:
                s[i][j] = i + 1
            elif j == 0:
                s[i][j] = 2
            elif i == 2:
                if isConvex([A[0],A[1],A[2]]):
                    s2[i][0] = A[0]
                    s2[i][1] = A[1]
                    s2[i][2] = A[2]
                    s[i][j] = 3
                else :
                    s[i][j] = 2
            elif i == j :
                s[i][j] = max (s[i])
            else :
                for k in range (0,j) :
                    if isConvex([A[k], A[j],A[i]]):
                        s2[i][j] = A[j]
                        s[i][j] = max (s[i][j] , s[j][k] + 1)
                    else :
                        #print(s[i][j])
                        s[i][j] = max ( s[i][j] , 2)
                        #print(s[i][j])
    result = 0
    finale = []
    for i in range (0, n):
        result = max ( result , s[i][i])
    
    for x in s2:
        y = [value for value in x if value !=0]
        if isConvex(y):
            if len(y) >= len(finale):
                finale = y
    
    return result


def combinations(items, lengthofLCS):
    

    return ( list(itertools.compress(items,mask)) for mask in itertools.product(*[[0,1]]*(lengthofLCS*2)) )
    


finalList = []

def convexhelper(filename, i, convexList):
    file1 = open(filename)
    A = [int(line.rstrip('\n')) for line in file1]
    #print(A)
    length = A[0]
    del A[0]
    #print(A)
    return A, length

def convex(A, i, convexList):
    #print(A)
    if i >= len(A)-1:
            return convexList
    elif A[i] < A[i+1]:
        if i == 0:
            convexList.append(A[i])
            return convex(A, i+1, convexList)
        
        elif A[i] > A[i+1]:
            return convex(A, i+1, convexList)
        else:
            if A[i+1] - A[i] > A[i] - A[i-1]: #between 2 and len(A)-1
                
                if i == len(A)-2:
                    convexList.append(A[i])
                    convexList.append(A[i+1])
                    return convex(A, i+1, convexList)
                else:
                    convexList.append(A[i])
                    return convex(A, i+1, convexList)
            else:
                return convex(A, i+1, convexList)
    else:
        return convex(A, i+1, convexList)

def main():
    a = []
    finale, listLength = convexhelper("input1.txt", 0, a)
    t0 = time.time()
    
    holder = []
    convexList = convex(finale, 0, a)
    test = solve(finale)
    if listLength <= 10:
        helperss = list(combinations(finale, test))
        for x in helperss:
            if len(x) <= test:
                if isConvex(x):
                    if len(x) > len(holder):
                        holder = x

    print(holder)
    print("Length of longest convex sequence is " + str(test)) 
    t1 = time.time()
    total = t1-t0
    print(total)

if __name__ == "__main__":
    main()