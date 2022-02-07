def upp(password):
    flag = 0
    for a in password:
        if a.isupper():
            flag = 1
    return flag


def dig(password):
    flag = 0
    for a in password:
        if a.isdigit():
            flag = 1
    return flag


def super(password):
    dic = [["qwertyuiop"], ["asdfghjkl"], ["zxcvbnm"], ["йцукенгшщзхъ"], ["фывапролджэ"], ["ячсмитьбю"]]
    flag_l = 1
    for i in range(len(password) - 2):
        a = password[i:i + 3]
        for d in range(len(dic)):
            b = str(dic[d])
            if b.find(a) != -1:
                flag_l = 0
    return flag_l


def test(password):
    assert upp(password), "error"
    assert dig(password), "error"
    assert super(password), "error"
    assert len(password) > 8, "error"

    print('ok')



print("Введите пароль: ")
password = input()
test(password)
