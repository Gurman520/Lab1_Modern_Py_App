from data import db_session
from data.tables import Job, User


def main(bd_name_m):
    len_rez = []
    lid_rez = []
    db_session.global_init(bd_name_m)
    db_sess = db_session.create_session()
    for job in db_sess.query(Job).filter():
        len_rez.append(len(job.collaborators))
        lid_rez.append(job.team_leader)
    for i in range(len(len_rez)):
        if len_rez[i] == max(len_rez):
            user = db_sess.query(User).filter(User.id == lid_rez[i]).first()
            print(user.surname, " ", user.name)


if __name__ == '__main__':
    bd_name = input("Введите название бд: ")
    main(bd_name)
