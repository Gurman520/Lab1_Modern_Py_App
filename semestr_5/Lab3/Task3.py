class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def upp(password):
    flag = 0
    for a in password:
        if a.isupper():
            flag = 1
    if flag == 0:
        raise LetterError("Нет заглавных букв")


def dig(password):
    flag = 0
    for a in password:
        if a.isdigit():
            flag = 1
    if flag == 0:
        raise DigitError("Нет ни одной цифры")


def leng(password):
    if len(password) < 8:
        raise LengthError("Слишком короткое")


def super(password):
    dic = [["qwertyuiop"], ["asdfghjkl"], ["zxcvbnm"], ["йцукенгшщзхъ"], ["фывапролджэ"], ["ячсмитьбю"]]
    for i in range(len(password) - 2):
        a = password[i:i + 3]
        for d in range(len(dic)):
            b = str(dic[d])
            if b.find(a) != -1:
                raise SequenceError("Нарушает требования последовательности")


def check_password(password):
    try:
        upp(password)
        dig(password)
        leng(password)
        super(password)
        print("ok")
    except PasswordError as e:
        print(e)


print("Введите пароль: ")
password = input()
check_password(password)
