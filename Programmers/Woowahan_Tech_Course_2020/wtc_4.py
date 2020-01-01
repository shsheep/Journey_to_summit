def solution(infos, actions):
    info_dict = dict()
    for inf in infos:
        id, pw = inf.split()
        info_dict[id] = pw
    logged_in = False
    basket_in = False
    answer = []
    for act in actions:
        tmp = act.split()
        # if case == "ADD" <= 직관적
        if len(tmp) == 1:
            if basket_in:
                answer.append(True)
                basket_in = False
            else:
                answer.append(False)
        elif len(tmp) == 2:
            if not logged_in:
                answer.append(False)
            else:
                answer.append(True)
                basket_in = True
        else:
            if logged_in:
                answer.append(False)
            else:
                t_id, t_pw = tmp[1], tmp[2]
                if t_id not in info_dict:
                    answer.append(False)
                elif info_dict[t_id] != t_pw:
                    answer.append(False)
                else:
                    answer.append(True)
                    logged_in = True

    return answer

print(solution(["kim password", "lee abc"], ["ADD 30", "LOGIN kim abc", "LOGIN lee password", "LOGIN kim password", "LOGIN kim password", "ADD 30", "ORDER", "ORDER", "ADD 40", "ADD 50"]))
