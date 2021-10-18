class NumberError(Exception):
    pass


class LengthError(NumberError):
    pass


class CodeError(NumberError):
    pass


class FormatError(NumberError):
    pass


class OperatorError(NumberError):
    pass


class phone:
    def operator(self, phone_number):
        flag = 0
        count = 0
        n = ''
        if phone_number[0] == '+' and phone_number[1] == '7':
            i = 2
            while count < 3:
                if phone_number[i].isdigit():
                    count += 1
                    n += phone_number[i]
                i += 1
        n = int(n)
        for z in range(902, 907, 1):
            if n == z:
                flag = 1
        for z in range(910, 940, 1):
            if n == z:
                flag = 1
        for z in range(960, 970, 1):
            if n == z:
                flag = 1
        for z in range(980, 990, 1):
            if n == z:
                flag = 1
        if flag == 0:
            raise OperatorError("не определяется оператор сотовой связи")




    def count_num(self, phone_number):
        count = 0
        for a in phone_number:
            if a.isdigit():
                count += 1
        if count != 11:
            raise LengthError("неверное количество цифр")


    def code_contre(self, phone_number):
        if (phone_number[0] != '+' or phone_number[1] != '7') and phone_number[0] != '8':
            raise CodeError("неверный код страны")


    def format(self, phone_number):
        flag = 0
        c = 0
        start = 0
        if phone_number[0] == '+':
            start = 1
        for i in range(start, len(phone_number), 1):
            if phone_number[i].isalpha():
                flag = 1
            if phone_number[i] != '-' and phone_number[i] != ' ' and phone_number[i] != '(' and phone_number[i] != ')' and not phone_number[i].isdigit():
                flag = 1
            if phone_number[i] == '(':
                c += 1
            if phone_number[i] == ')':
                c -= 1
        if c != 0 or flag == 1:
            raise FormatError("неверный формат")


    def preobr(self, phone_number):
        N = ''
        start = 1
        if phone_number[0] == '+':
            N += phone_number[0] + phone_number[1]
            start = 2
        else:
            N += phone_number[0]
        for i in range(start, len(phone_number), 1):
            if phone_number[i].isdigit():
                N += phone_number[i]
        return N


    def check_number(self, phone_number):
        try:
            self.format(phone_number)
            self.count_num(phone_number)
            self.code_contre(phone_number)
            self.operator(phone_number)
            return self.preobr(phone_number)
        except NumberError as e:
            return e