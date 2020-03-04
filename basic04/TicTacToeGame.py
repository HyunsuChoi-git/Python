# Tic Tac Toe
# 가로/세로/대각선으로 3개 먼저 채우는 사람이 승리
# 플레이어가 X / O 중 선택
# 누가 먼저할지 random
# 승리했는지 체크

import random

# ***보드 출력***
# board는 10개 문자열로 된 리스트, 텐키배열, board[0]은 무시
def drawBoard(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-----------")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('X를 하고 싶나요, O를 하고 싶나요?: ')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('게임을 다시 하겠습니다? (y / n)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le): 
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or  #가로 윗줄
        (bo[4] == le and bo[5] == le and bo[6] == le) or  #가로 중간줄
        (bo[1] == le and bo[2] == le and bo[3] == le) or  #가로 밑줄
        (bo[7] == le and bo[4] == le and bo[1] == le) or  #세로 왼쪽
        (bo[8] == le and bo[5] == le and bo[2] == le) or  #세로 중간
        (bo[9] == le and bo[6] == le and bo[3] == le) or  #세로 오른쪽
        (bo[7] == le and bo[5] == le and bo[3] == le) or  #대각선 왼부터
        (bo[9] == le and bo[5] == le and bo[1] == le)  #대각선 오부터
    )

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("어디에 마크할까요? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList): 
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):               
            possibleMoves.append(i)             

    if len(possibleMoves) != 0:                 
        return random.choice(possibleMoves)    
    else:
        return None                            

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

  
    for i in range(1, 10):             
        copy = getBoardCopy(board)      
        if isSpaceFree(copy, i):       
            makeMove(copy, computerLetter, i)   
            if isWinner(copy, computerLetter):  
                return i                      

    for i in range(1, 10):             
        copy = getBoardCopy(board)     
        if isSpaceFree(copy, i):        
            makeMove(copy, playerLetter, i)    
            if isWinner(copy, playerLetter):    
                return i                        

 
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) 
    if move != None:       
        return move        
 
    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i): 
            return False           
    return  True


print("틱택토 게임!!")


while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()  
    turn = whoGoesFirst()   
    print(turn + '가 먼저 시작하겠습니다.')
    gameIsPlaying = True   

    while gameIsPlaying:   
        if turn == 'player':
            drawBoard(theBoard)    
            move = getPlayerMove(theBoard)  
            makeMove(theBoard, playerLetter, move)  

            if isWinner(theBoard, playerLetter):   
                drawBoard(theBoard)                
                print("하하하 이겼다!!")
                gameIsPlaying = False
            else:                                 
                if isBoardFull(theBoard):          
                    drawBoard(theBoard)            
                    print("비겼네..")
                    break                       
                else:
                    turn = 'computer'          

        else:
            move = getComputerMove(theBoard, computerLetter) 
            makeMove(theBoard, computerLetter, move)         

            if isWinner(theBoard, computerLetter):  
                drawBoard(theBoard)
                print("졌어 ㅠㅠ 컴퓨터 승리 ㅠㅠ")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):          
                    drawBoard(theBoard)
                    print("비겼네....")
                    break
                else:
                    turn = 'player'               

    if not playAgain():
        print("끝!")
        break


















