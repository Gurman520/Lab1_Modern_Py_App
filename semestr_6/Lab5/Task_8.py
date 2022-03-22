from data import db_session
from data.tables import Job


def main(bd_name_m):
    db_session.global_init(bd_name_m)
    db_sess = db_session.create_session()
    for job in db_sess.query(Job).filter(Job.work_size < 20, Job.is_finished != True):
        print(job)


if __name__ == '__main__':
    bd_name = input("Введите название бд: ")
    main(bd_name)
