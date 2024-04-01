#The algorithm finds the position of the 2 rooks with the highest sum of checkered fields
def fun(T):
    n = len(T)
    def rek(x=-1,y=-1,q= 0):
        rows = []
        columns = []
        for i in range(n):
            row = []
            column = []
            for j in range(n):
                row.append(T[i][j])
                column.append(T[j][i])
            rows.append(row)
            columns.append(column)
        row_sum = column_sum = float("-inf")
        maxrow = 0
        maxcolumn = 0
        for i in range(n):
            if sum(rows[i]) > row_sum:
                row_sum = sum(rows[i])
                maxrow = i
            if sum(columns[i]) > column_sum:
                column_sum = sum(columns[i])
                maxcolumn = i
        for i in range(n):
            for j in range(n):
                if i == maxrow or j == maxcolumn:
                    if i == maxrow and j == maxcolumn:
                        continue
                    T[i][j] = 0
        if q == 0:
            return (maxrow,maxcolumn),rek(-1,-1,1)
        return (maxrow,maxcolumn)
    return rek(-1,-1)
T = [[1,2,3],[4,5,6],[7,8,9]]   #chessboard
print(fun(T))
