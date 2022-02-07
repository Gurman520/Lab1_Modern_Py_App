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


class pas:
    def upp(self, password):
        flag = 0
        for a in password:
            if a.isupper():
                flag = 1
        if flag == 0:
            raise LetterError("Нет заглавных букв")

    def dig(self, password):
        flag = 0
        for a in password:
            if a.isdigit():
                flag = 1
        if flag == 0:
            raise DigitError("Нет ни одной цифры")

    def leng(self, password):
        if len(password) < 8:
            raise LengthError("Слишком короткое")

    def super(self, password):
        dic = [["qwertyuiop"], ["asdfghjkl"], ["zxcvbnm"], ["йцукенгшщзхъ"], ["фывапролджэ"], ["ячсмитьбю"]]
        for i in range(len(password) - 2):
            a = password[i:i + 3]
            for d in range(len(dic)):
                b = str(dic[d])
                if b.find(a) != -1:
                    raise SequenceError("Нарушает требования последовательности")

    def check_password(self, password):
        try:
            self.upp(password)
            self.dig(password)
            self.leng(password)
            self.super(password)
            return 1
        except PasswordError as e:
            return e