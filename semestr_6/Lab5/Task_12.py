from data import db_session
from data.tables import User, Job, Department


def main(bd_name_m):
    db_session.global_init(bd_name_m)
    db_sess = db_session.create_session()
    for dept in db_sess.query(Department).filter(Department.id == 1):
        summ = 0
        for item in dept.members:
            for job in db_sess.query(Job).filter():
                for use in job.collaborators:
                    if item.id == use.id:
                        summ += job.work_size
            if summ > 25:
                print(item.name)


if __name__ == '__main__':
    bd_name = input("Введите название бд: ")
    main(bd_name)
