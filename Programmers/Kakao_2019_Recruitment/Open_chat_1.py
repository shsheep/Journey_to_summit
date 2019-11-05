def solution(record):
    answer = []
    user_dict = dict()
    for r in record:
        tx = r.split()
        if tx[0] == "Enter" or tx[0] == "Change":
            _, uid, name = tx
            user_dict[uid] = name
    for r in record:
        tx = r.split()
        uid = tx[1]
        if tx[0] == "Enter":
            answer.append(user_dict[uid] + "님이 들어왔습니다.")
        elif tx[0] == "Leave":
            answer.append(user_dict[uid] + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))