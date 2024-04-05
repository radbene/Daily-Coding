#The algorithm returns the minimum number of moves of the rook placed on the chessboard
#to reach coordinates[n-1,n-1], where nxn is the size of the chessboard
#You place the rook as well as the pawns that can block the rooks path
#Rook can't go backwards
def fun(rook,chessboard,pawns):
    n = len(chessboard)
    def rek(x=0,y=0,count=0):
        a = b = float("inf")
        if x == n-1 and y == n-1:
            return count
        for i in range(n-1,x,-1):   #check horizontal movements from longest to shortest
            is_free = True
            for pawn in pawns:
                if y == pawn[1] and i >= pawn[0] and pawn[0] >= x:    #check if any pawn stands in the way
                    is_free = False
            if is_free:
                a = min(rek(i,y,count + 1),a)
        for j in range(n-1,y,-1):   ##check vertical movements from longest to shortest
            is_free = True
            for pawn in pawns:
                if x == pawn[0] and j >= pawn[1] and pawn[1] >= y:    #check if any pawn stands in the way
                    is_free = False
            if is_free:
                b = min(rek(x,j,count + 1),b)
        if a == float("inf") and b == float("inf"): #if the rook cannot get into the (n-1,n-1) field
            return "There are no legal moves"
        return min(a,b)     #return the smallest of the number of moves
    return rek(rook[0],rook[1])

def setup():
    n = int(input("The rook at the beginning is located on the field [0,0]\nSpecify the size of the chessboard:\n"))
    if n < 1 or n % 1 != 0:
        print("Size of the chessboard must be a positive integer")
        return
    b = int(input("specify x-position of rook(only values 0 to n-1 are accepted)\n"))
    a = int(input("specify y-position of rook(only values 0 to n-1 are accepted)\n"))
    if a < 0 or a % 1 != 0 or a > n - 1 or b < 0 or b % 1 != 0 or b > n - 1:
        print("invalid pawn position")
        return
    rook = [b,a]
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    chessboard[rook[1]][rook[0]] = 'W'
    pawns = []
    while input("Do you want to add pawns to the chessboard?\nY - yes\nn - no\n") == "Y":
        x = int(input("specify x-position of pawn(only values 0 to n-1 are accepted)\n"))
        y = int(input("specify y-position of pawn(only values 0 to n-1 are accepted)\n"))
        if x < 0 or x % 1 != 0 or x > n-1 or y < 0 or y % 1 != 0 or y > n-1:
            print("invalid pawn position")
            return
        if y == rook[1] and x == rook[0]:
            print("You cant place pawn on the rook")
            return
        pawns.append([x,y])
    print(pawns)
    #visualization of a chessboard
    for pawn in pawns:
        chessboard[pawn[1]][pawn[0]] = 1
    for row in chessboard:
        print(row)
    print(fun(rook,chessboard, pawns))

setup()