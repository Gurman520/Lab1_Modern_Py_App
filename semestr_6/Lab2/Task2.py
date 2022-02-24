import sys
import os.path


def main(args):
    sort = 0
    num = 0
    count = 0
    while args:
        arg = args.pop(0)
        if arg == '--sort':
            sort = 1
        elif arg == '--num':
            num = 1
        elif arg == '--count':
            count = 1
        else:
            if not os.path.isfile(arg):
                print("Error")
            else:
                str = []
                with open(arg) as file:
                    for line in file:
                        str.append(line)
                if sort == 1:
                    str.sort()
                if num == 1:
                    co = 0
                    for i in range(len(str)):
                        str[i] = f'{co} ' + str[i]
                        co += 1
                if count == 1:
                    str.append("Количество строк: " + f'{len(str)}')
                for s in str:
                    print(s, end='')


main(sys.argv[1:])
