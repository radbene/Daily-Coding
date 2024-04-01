#the algorithm finds a path through the fields
#with the highest sum from the first row to the last on the chessboard for the king

def fun(T):
    n = len(T)
    def rek(column=0,row= 0,sum = 0):
        if row == n-1:
            return sum + T[row][column]
        sum += T[row][column]
        a = b = float("-inf")
        if column > 0:
            a = rek(column-1,row+1,sum)
        if column < n-1:
            b = rek(column+1,row+1,sum)
        c = rek(column,row+1,sum)
        return max(a,b,c)   #pick the highest sum
    maxsum = rek(0)  #select the column from which the king will start the path(0 - 1st, 8 - last)
    return maxsum

T=[[i for i in range(1,10)] for _ in range(9)]  #chessboard
print(T)
print(fun(T))