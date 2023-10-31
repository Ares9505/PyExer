#Ejer name Valid Sudoku:
def checkForRepeticion(current_list: list) -> bool :
    validation = True
    temp_list = []
    for i in current_list:
        if i != ".":
            if i in temp_list:
                validation = False
            else:
                temp_list.append(i)
    return validation


def ValidSudoku(board: list[list[str]]) -> bool:    
    temp_list = []
    
    for k in range(0,9):
        if checkForRepeticion(board[k]) == False:
            return False

    for i in range(0,9):
        for j in range(0,9):
            temp_list.append(board[j][i])
        if  checkForRepeticion(temp_list)== False:
            return False   
        temp_list = []

    i=0
    j=0
    temp_list = [] 

    while i<7:
        while j<7:
            for row in board[i:i+3]:
                temp_list += row[j:j+3]
            if checkForRepeticion(temp_list) ==False:
                return False
            temp_list=[]
            j+=3
        j=0
        i+=3   

    return True



input1 = [["5","3",".",".","7",".",".",".","."] 
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,[".",".",".","4","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

input2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(ValidSudoku(input1))
