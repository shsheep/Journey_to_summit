# Rotate the board clockwise for better list approach
def rotate(board: list):
    width, height = len(board[0]), len(board)
    ret = [[0] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            ret[x][y] = board[height-y-1][x]
    return ret


def solution(board, moves):
    moves = [num-1 for num in moves]
    for b in board:
        print(b)
    print()
    theMap = rotate(board)
    for t in theMap:
        print(t)

    answer = 0
    stack = []
    for m in moves:
        found = False
        # Find the last head of the m-th line
        for i in range(len(theMap[0])-1, -1, -1):
            if theMap[m][i] != 0:
                head = theMap[m][i]
                theMap[m][i] = 0
                found = True
                break
        if not found:
            continue
        stack.append(head)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2


    return answer

# # Rotate the board clockwise for better list approach
# def rotate(board: list):
#     width, height = len(board[0]), len(board)
#     ret = [[0] * height for _ in range(width)]
#     for x in range(width):
#         for y in range(height):
#             ret[x][y] = board[height-y-1][x]
#     return ret
#
#
# def solution(board, moves):
#     moves = [num-1 for num in moves]
#     theMap = rotate(board)
#     answer = 0
#     stack = []
#     for m in moves:
#         found = False
#         # Find the last head of the m-th line
#         for i in range(len(theMap[0])-1, -1, -1):
#             if theMap[m][i] != 0:
#                 head = theMap[m][i]
#                 theMap[m][i] = 0
#                 found = True
#                 break
#         if not found:
#             continue
#         stack.append(head)
#         if len(stack) >= 2 and stack[-1] == stack[-2]:
#             stack.pop()
#             stack.pop()
#             answer += 2
#
#     return answer



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1],[1,2,3,4,5]], [1,5,3,5,1,2,1,4]))
