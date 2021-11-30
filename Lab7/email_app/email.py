def fun(s):
    flag = 0
    s = s.lower()
    dog = s.find("@")
    if dog == 0 or dog == len(s) or dog == -1:
        flag = 1
    for i in range(dog):
        if s[i].isdigit() or 97 <= ord(s[i]) <= 122 or s[i] == '_' or s[i] == '-':
            pass
        else:
            flag = 1
    point = s.find(".")
    if len(s) - point > 4:
        flag = 1
    for i in range(dog + 1, point):
        if s[i].isdigit() or 97 <= ord(s[i]) <= 122:
            pass
        else:
            flag = 1
    if flag == 1:
        return False
    return True


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))
