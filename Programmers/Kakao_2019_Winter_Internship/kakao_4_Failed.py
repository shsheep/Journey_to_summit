def solution(k, room_number):
    room = [0] * (k+1)
    answer = []
    for idx, num in enumerate(room_number):
        if room[num] == 0:
            answer.append(num)
            room[num] += 1
        else:
            tmp = num+1
            while True:
                if room[tmp] == 0:
                    room[tmp] = 1
                    answer.append(tmp)
                    break
                tmp += 1
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [1, 3, 4, 1, 3, 6, 7]))
