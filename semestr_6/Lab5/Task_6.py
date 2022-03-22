from data import db_session
from data.tables import User


def main(bd_name_m):
    db_session.global_init(bd_name_m)
    db_sess = db_session.create_session()
    for use in db_sess.query(User).filter(User.age < 18):
        print(use, f" {use.age} лет")


if __name__ == '__main__':
    bd_name = input("Введите название бд: ")
    main(bd_name)
