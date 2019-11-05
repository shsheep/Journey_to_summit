def solution(board):
    answer = 0
    types = [[], [], [], [], []]
    N, M = len(board), len(board[0])
    for x in range(N):
        if len(set(board[x])) == 1:
            continue
        for y in range(M):
            val = board[x][y]
            if val == 0:
                continue
            if x < N-1 and y < M-2 and val == board[x+1][y] and val == board[x+1][y+1] and \
                    val == board[x+1][y+2]:
                types[0].append((x, y))
            elif x < N-2 and y > 0 and val == board[x+1][y] and val == board[x+2][y] and \
                    val == board[x+2][y-1]:
                types[1].append((x, y))
            elif x < N-2 and y < M-1 and val == board[x+1][y] and val == board[x+2][y] and \
                    val == board[x+2][y+1]:
                types[2].append((x, y))
            elif x < N-1 and y > 1 and val == board[x+1][y] and val == board[x+1][y-1] and \
                    val == board[x+1][y-2]:
                types[3].append((x, y))
            elif x < N-1 and 0 < y < M - 1 and val == board[x + 1][y] and val == board[x + 1][y - 1] and \
                    val == board[x+1][y+1]:
                types[4].append((x, y))
    broken = True
    while broken:
        broken = False
        for i in range(len(types)):
            if not types[i]:
                continue
            to_remove = []
            if i == 0:
                for idx, c in enumerate(types[i]):
                    x, y = c[0], c[1]
                    check_y = [y+1, y+2]
                    for dy in check_y:
                        fail = False
                        for dx in range(x, -1, -1):
                            if board[dx][dy] != 0:
                                fail = True
                                break
                        if fail:
                            break
                    if not fail:
                        to_remove.append(idx)
                        board[x][y] = board[x+1][y] = board[x+1][y+1] = board[x+1][y+2] = 0
                        broken = True
                        answer += 1
                types[i] = list(filter(lambda tup: types[i].index(tup) not in to_remove, types[i]))
            elif i == 1:
                for idx, c in enumerate(types[i]):
                    x, y = c[0], c[1]
                    check_y = [y-1]
                    for dy in check_y:
                        fail = False
                        for dx in range(x+1, -1, -1):
                            if board[dx][dy] != 0:
                                fail = True
                                break
                        if fail:
                            break
                    if not fail:
                        to_remove.append(idx)
                        board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y-1] = 0
                        broken = True
                        answer += 1
                types[i] = list(filter(lambda tup: types[i].index(tup) not in to_remove, types[i]))

            elif i == 2:
                for idx, c in enumerate(types[i]):
                    x, y = c[0], c[1]
                    check_y = [y+1]
                    for dy in check_y:
                        fail = False
                        for dx in range(x+1, -1, -1):
                            if board[dx][dy] != 0:
                                fail = True
                                break
                        if fail:
                            break
                    if not fail:
                        to_remove.append(idx)
                        board[x][y] = board[x+1][y] = board[x+2][y] = board[x+2][y+1] = 0
                        broken = True
                        answer += 1
                types[i] = list(filter(lambda tup: types[i].index(tup) not in to_remove, types[i]))
                        
            elif i == 3:
                for idx, c in enumerate(types[i]):
                    x, y = c[0], c[1]
                    check_y = [y-2, y-1]
                    for dy in check_y:
                        fail = False
                        for dx in range(x, -1, -1):
                            if board[dx][dy] != 0:
                                fail = True
                                break
                        if fail:
                            break
                    if not fail:
                        to_remove.append(idx)
                        board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y-2] = 0
                        broken = True
                        answer += 1
                types[i] = list(filter(lambda tup: types[i].index(tup) not in to_remove, types[i]))

            else:
                for idx, c in enumerate(types[i]):
                    x, y = c[0], c[1]
                    check_y = [y-1, y+1]
                    for dy in check_y:
                        fail = False
                        for dx in range(x, -1, -1):
                            if board[dx][dy] != 0:
                                fail = True
                                break
                        if fail:
                            break
                    if not fail:
                        to_remove.append(idx)
                        board[x][y] = board[x+1][y] = board[x+1][y-1] = board[x+1][y+1] = 0
                        broken = True
                        answer += 1
                types[i] = list(filter(lambda tup: types[i].index(tup) not in to_remove, types[i]))

    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 0, 0], [1, 1, 1, 3, 2, 2, 2], [0, 0, 3, 3, 3, 0, 4], [0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 4, 4]]))
