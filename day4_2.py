# read input file
file = open('input/day4.txt', 'r')
input = file.readlines()

# body of solution

def isBoardWinner(board):
    for i in range(5):
        if sum(board[i]) == -5:
            return True
    for i in range(5):
        if (board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i]) == -5:
            return True
    return False

def sumRemaining(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                sum += board[i][j]
    return sum

def doBingo(drawnNums, boards, winners):
    ## simulate bingo round
    for drawn in drawnNums:
        for b in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if not winners[b] and boards[b][i][j] == drawn:
                        boards[b][i][j] = -1
                        if isBoardWinner(boards[b]):
                            winners[b] = True
                            if winners.count(False) == 0:
                                return drawn * sumRemaining(boards[b])

def initBoards():
    boards = []
    currBoard = 0
    currLine = 0
    for line in input[2:]:
        if line.isspace():
            continue
        if currLine == 0:
            boards.append([])
        boards[currBoard].append(list(map(int, filter(None, line.strip().split(' ')))))
        currLine += 1
        if currLine == 5:
            currBoard += 1
            currLine = 0
    return boards

drawnNums = list(map(int, input[0].strip().split(',')))
boards = initBoards()
winners = []
for i in range(len(boards)):
    winners.append(False)
print(doBingo(drawnNums, boards, winners))