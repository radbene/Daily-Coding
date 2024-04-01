#algorithm counts the number of different arrangements of n queens on a chessboard of size n x n and prints them out
def fun(Q,w,n):
    count = 0
    def rek(Q,row,n):
        nonlocal count
        if row == n:    #if this is the last row then come back
            count += 1
            print(Q)    #Print queens coordinates
            return
        for i in range(n): #for each field in the row check if any queen is checking it
            free = True
            for queen in Q: #checking if the current field is checked
                if row == queen[0] or i == queen[1] or row + i == queen[0] + queen[1] or row - i == queen[0] - queen[1]: #sprawdzanie po skosach
                    free = False
            if free: #if the field is free, then go further into the recursion and then delete the last step
                Q.append((row,i))
                rek(Q,row + 1,n)
                Q.pop()
        return #there are no more legal steps in this line so come back
    rek(Q,w,n)
    print(count)

Q =[] #list of sorted queens as tuples of coordinates
n = int(input("Input the size of the array\n"))
fun(Q,0,n)

