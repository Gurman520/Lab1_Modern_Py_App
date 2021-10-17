dic = [["qwertyuiop"], ["asdfghjkl"], ["zxcvbnm"], ["йцукенгшщзхъ"], ["фывапролджэ"], ["ячсмитьбю"]]

def test(password):
    flag_l = 0
    for i in range(len(password) - 2):
        a = password[i:i+3]
        for d in range(len(dic)):
            b = str(dic[d])
            if b.find(a) != -1:
                flag_l = 1
    flag_A = 0
    flag_di = 0
    for a in password:
        if a.isupper():
            flag_A = 1
        if a.isdigit():
            flag_di = 1
    if len(password) > 8 and flag_A == 1 and flag_di == 1 and flag_l == 0:
        print("Ok")
    else:
        print("error")


print("Введите пароль: ")
password = input()
test(password)
