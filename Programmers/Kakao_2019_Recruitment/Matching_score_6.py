import re

def solution(word, pages):
    word = word.lower()
    exp = re.compile('[a-zA-Z]+')
    urls = []
    basic_score = []
    external_links = [0] * len(pages)
    referenced = dict()
    for i, p in enumerate(pages):
        tmp = p.split()
        url_ready = get_url = False
        ref_ready = False
        for x in tmp:
            if get_url:
                print("HERE IS URL OF CURRENT PAGE ", x)
                quotes = x.index("\"")
                u = x[quotes+1:-3]
                urls.append(u)
                url_ready = get_url = False
                continue
            if not url_ready and x == "<meta":
                url_ready = True
                continue
            elif url_ready and x[-4:-1] == "url":
                get_url = True
                continue
            else:
                url_ready = False

            if ref_ready and '\"' in x:
                start_quotes = x.index('\"')
                end_quotes = start_quotes + x[start_quotes+1:].index('\"')
                refer_url = x[start_quotes+1:end_quotes+1]
                external_links[i] += 1
                if refer_url in referenced:
                    referenced[refer_url].append(urls[-1])
                else:
                    referenced[refer_url] = [urls[-1]]
                print("HERE IS REFERENCING PAGE ", x[start_quotes+1:end_quotes])
                # print(start_quotes, end_quotes)
                # print(x[start_quotes:])
                ref_ready = False
            else:
                ref_ready = False
            if "<a" in x:
                ref_ready = True
            print(x)
        # print("=========END OF REFERENCE CHECKING==========")
        score = 0
        result = exp.findall(p)
        for x in result:
            if x.lower() == word:
                score += 1
            print(x)
        basic_score.append(score)
    #     print("= = = = = = = END OF SEARCHING WORD = = = = = = = = =")
    # print(urls, external_links)
    # print(referenced)
    # print(basic_score)
    answer = []
    for i, u in enumerate(urls):
        link_score = 0.0
        if u in referenced:
            for link in referenced[u]:
                idx = urls.index(link)
                link_score += float(basic_score[idx]) / external_links[idx]
        answer.append(basic_score[i] + link_score)
    ret = answer.index(max(answer))
    return ret


# print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<hfxtml lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
