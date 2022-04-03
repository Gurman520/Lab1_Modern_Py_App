from data import db_session
from data.tables import Job, User, Department, Category


def add_user(surname, name, age, position, speciality, addres, email, password):
    user_n = User()

    user_n.surname = surname
    user_n.name = name
    user_n.age = age
    user_n.position = position
    user_n.speciality = speciality
    user_n.addres = addres
    user_n.email = email
    if password != '':
        user_n.set_password(password)

    db_sess = db_session.create_session()
    db_sess.add(user_n)
    db_sess.commit()


def add_jobs(team_leader, job, work_size, collaborator, categ, start_date, end_date, is_finished):
    job_n = Job()
    db_sess = db_session.create_session()

    job_n.team_leader = team_leader
    job_n.job = job
    job_n.work_size = work_size
    for i in collaborator:
        user = db_sess.query(User).filter(User.id == i).first()
        job_n.collaborators.append(user)
    for c in categ:
        cat = db_sess.query(Category).filter(Category.id == c).first()
        job_n.categories.append(cat)
    if start_date is not None:
        job_n.start_date = start_date
    if start_date is not None:
        job_n.end_date = end_date
    job_n.is_finished = is_finished

    db_sess.add(job_n)
    db_sess.commit()


def add_department(title, chief, members, email):
    dept_n = Department()
    db_sess = db_session.create_session()

    dept_n.title = title
    dept_n.chief = chief
    for i in members:
        user = db_sess.query(User).filter(User.id == i).first()
        dept_n.members.append(user)
    dept_n.email = email

    db_sess.add(dept_n)
    db_sess.commit()


def add_categorie(name):
    cat_n = Category()
    db_sess = db_session.create_session()

    cat_n.name = name

    db_sess.add(cat_n)
    db_sess.commit()

def main():
    db_session.global_init("db/mars_explorer.db")
    # добавление записи
    add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org", "hfcgbcfybt")
    add_user("Eps", "Omar", 25, "engineer", "civil engineer", "module_2", "Omar@mars.org", "")
    add_user("Vilsan", "Ridley", 29, "pilot", "research engineer", "module_2", "pilot_master_Vil@mars.org", "")
    add_user("House", "Greg", 40, "engineer", "engineer", "module_2", "Greg_H@mars.org", "")
    add_user("Forman", "Eric", 24, "chief doctor", "surgeon", "module_2", "forman_doctor@mars.org", "")
    add_user("Scott", "Liza", 19, "biologist", "engineer biologistr", "module_1", "scott_liza@mars.org", "")
    add_user("Scott", "Saymon", 17, "middle doctor", "doctor", "module_1", "Saimon_Sc@mars.org", "")
    add_user("Scott", "Sofi", 15, "Passenger", "Passenger", "module_1", "scott_sofi@mars.org", "")
    add_categorie("building")
    add_categorie("learning")
    add_categorie("other")
    add_categorie("team")
    add_categorie("single")
    add_jobs(1, "deployment of residential modules 1 and 2", 15, [2, 3], [1, 3], None, None, False)
    add_jobs(1, "deployment of residential modules 3", 9, [2, 4], [2, 3], None, None, False)
    add_jobs(1, "Setting up a life support system", 40, [7, 8, 4], [3, 1], None, None, False)

    add_department("геологическая разведка", 3, [2, 5, 4], "geolog_raz@mars.org")


if __name__ == '__main__':
    main()
