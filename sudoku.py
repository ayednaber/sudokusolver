import pygame
from pygame.constants import K_SPACE

pygame.init()
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Sudoku')
background = pygame.image.load('background.jpg')

def find_next_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None, None # this means that the board is solved
def is_valid(board, guess, row, col):
    # Checking row validity
    row_vals = board[row]
    if guess in row_vals:
        return False
    
    # Checking column validity
    col_vals = []
    for i in range(9):
        col_vals.append(board[i][col])
    if guess in col_vals:
        return False

    # 3x3 matrix validity
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False
    
    return True # If we passed all checks, we just return True
    
def sudoku_solver(board):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    # Step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(board)
    # Step 1.1: if there is nowhere left, then we are done because we only allowed valid inputs
    if row is None:
        return True # this means that we have solved our puzzle
    # Step 2: If there is a place to put a number, then make a guess between 1-9
    for guess in range(1, 10):
        # Step 3: Checking if this is a valid guess
        if is_valid(board, guess, row, col):
            # Step 3.1: if this is valid, then place that guess on the puzzle!
            board[row][col] = guess
            # now recurse using the puzzle
            # step 4: recursively call our function
            if sudoku_solver(board):
                return True
        # Step 5: if not valid OR if our guess does not solve the puzzle, then we need to backtrack and try a new number
        board[row][col] = 0
    # Step 6: if none of the numbers that we try work, then this puzzle is unsolvable!
    return False

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

font = pygame.font.SysFont('Calibri', 32)

run = True
while run:
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    welcome_text = font.render("Welcome to the Sudoku Solver!", 1, (0, 0, 0))
    solve_text = font.render("Press SPACE to solve the Sudoku board", 1, (0, 0, 0))
    win.blit(welcome_text, (130, 20))
    win.blit(solve_text, (110, 655))
    pygame.draw.line(win, (0, 0, 0), (18, 60), (18, 635), 3) # Left vertical line
    pygame.draw.line(win, (0, 0, 0), (677, 60), (677, 637), 3) # Right vertical line
    pygame.draw.line(win, (0, 0, 0), (18, 58), (677, 58), 3) # Top horizontal line
    pygame.draw.line(win, (0, 0, 0), (18, 637), (675, 637), 3) # Bottom horizontal line

    # Thicker lines to distinguish between 3x3 boxes
    pygame.draw.line(win, (0, 0, 0), (20, 250), (675, 250), 3)
    pygame.draw.line(win, (0, 0, 0), (20, 445), (675, 445), 3)
    pygame.draw.line(win, (0, 0, 0), (235, 60), (235, 635), 3)
    pygame.draw.line(win, (0, 0, 0), (460, 60), (460, 635), 3)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                sudoku_solver(board)
    
    y = 60
    for i in range(len(board)):
        x = 20
        for j in range(9):
            pygame.draw.rect(win, (255, 255, 255), (x,y,56,56))
            pygame.draw.rect(win, (0, 0, 0), (x, y, 56, 56), 1)
            if (board[i][j] != 0):
                text = font.render(str(board[i][j]), 1, (0, 0, 0))
                win.blit(text, (x + 18, y + 11))
            x += 75
        y += 65
        
    pygame.display.update()
pygame.quit()



