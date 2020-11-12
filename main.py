# grid
def printboard(board):
    print(' 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9')
    print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    for i in range(len(board)):
        print('|' + ' '.join(board[i]) + '|' + str(i))
    print(' - - - - - - - - - - - - - - - - - - - - ')
    print(' 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9')


def firstword(board, word):
    if len(word) > len(board):
        return False
    else:
        for k in range(len(word)):
            column = len(board) // 2 - len(word) // 2 + k
            board[len(board) // 2][column] = word[k]
        return True


# VERTICAL -------------------------------------------------------

def checkvertical(board, word, row, col):
    matchesoneletter = False
    # checks for out of range
    if len(word) > 20 - row:
        return False
    for i in range(len(word)):
        wordletter = word[i]
        boardletter = board[row + i][col]
        #  checks if there's a matching letter
        if wordletter == boardletter:
            matchesoneletter = True
        if boardletter == ' ':
            # checks adjacents
            if col != 19:
                if board[row + i][col + 1] != ' ':
                    return False
            if col != 0:
                if board[row + i][col - 1] != ' ':
                    return False
        # checks end caps
        if row > 0 and board[row - 1][col] != ' ':
            return False
        if row + len(word) - 1 < 19 and board[row + len(word)][col] != ' ':
            return False
        # checks for overlaps
        if i < len(word) - 1:
            if board[row + i][col] != ' ' and board[row + i + 1][col] != ' ':
                return False
    return matchesoneletter


def addvertical(board, word):
    for i in range(len(board)):
        for j in range(len(board)):
            if checkvertical(board, word, i, j):
                for k in range(len(word)):
                    board[i + k][j] = word[k]
                return True
    return False


# HORIZONTAL ---------------------------------

def checkhorizontal(board, word, row, col):
    """Function is similar to checkvertical, except this will check the legality of placing a horizontal

    :param board: grid
    :param word: a word
    :param row: a row coordinate of the matrix
    :param col: a column coordinate of the matrix
    :return: True or False for addhorizontal function
    """
    matchesoneletter = False
    if len(word) > 20 - col:
        return False
    for i in range(len(word)):
        wordletter = word[i]
        boardletter = board[row][col + i]
        # if there's a matching letter
        if wordletter == boardletter:
            matchesoneletter = True
        if boardletter == ' ':
            # checks adjacencies
            if row != 19:
                if board[row + 1][col + i] != ' ':
                    return False
            if row != 0:
                if board[row - 1][col + i] != ' ':
                    return False
        # checks end caps
        if col > 0 and board[row][col - 1] != ' ':
            return False
        if col + len(word) - 1 < 19 and board[row][col + len(word)] != ' ':
            return False
        # overlaps
        if i < len(word) - 1:
            if board[row][col + i] != ' ' and board[row][col + i + 1] != ' ':
                return False
    return matchesoneletter


def addhorizontal(board, word):
    """if checkhorizontal is True, addhorizontal commenses

    :param board: Grid
    :param word: The word being placed
    :return: True or False, and places the word horizontally
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if checkhorizontal(board, word, i, j):
                for k in range(len(word)):
                    board[i][j + k] = word[k]
                return True
    return False


# CROSSWORDS

def crossword(words):
    vertical = False
    b = [[' '] * 20 for i in range(20)]
    firstword(b, words[0])
    for j in words[1:]:
        if not vertical:
            # alternating orientation in case addvertical can't occur
            if addvertical(b, j) is False:
                vertical = False
                if addhorizontal(b, j) is False:
                    print('no matching letter / illegal adjacencies / reaches outside grid :', j)
            else:
                vertical = True
        else:
            # alternating orientation in case addhorizontal can't occur
            if addhorizontal(b, j) is False:
                vertical = True
                if addvertical(b, j) is False:
                    print('no matching letter / illegal adjacencies / reaches outside grid :', j)
            else:
                vertical = False
    printboard(b)


# OUTPUT

L = ['tarvern', 'tonton', 'takoyaki', 'octopus', 'pho']
crossword(L)
