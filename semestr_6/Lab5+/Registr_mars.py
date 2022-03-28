from flask import Flask, render_template, redirect
from data import db_session
from data.tables import Job, User, Department
from loginform import LoginForm
from reg_job import JobForm
from reg_dept import DeptForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Job)
    return render_template("index.html", title="Works log", job=job)


@app.route("/job_register", methods=['GET', 'POST'])
def job_register():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(Job).filter(Job.job == form.job.data).first():
            return render_template('job_register.html', title='Регистрация',
                                   form=form,
                                   message="Такая работа уже есть")
        job = Job()
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.team_leader = form.team_leader.data
        coll_str = form.collaborators.data
        coll_str = coll_str.split()
        for i in coll_str:
            user = db_sess.query(User).filter(User.id == i).first()
            job.collaborators.append(user)
        if form.start_date.data != "":
            job.start_date = form.start_date.data
        if form.end_date.data != "":
            job.end_date = form.end_date.data
        job.is_finished = False
        if form.is_finished.data is True:
            job.is_finished = True
        db_sess.add(job)
        db_sess.commit()
        return redirect('/login')
    return render_template('job_register.html', title='Регистрация работы', form=form)


@app.route("/dept_register", methods=['GET', 'POST'])
def dept_register():
    form = DeptForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(Department).filter(Department.email == form.email.data).first():
            return render_template('dept_registr.html', title='Регистрация',
                                   form=form,
                                   message="Такой департамент уже есть")
        dept = Department()
        dept.title = form.title.data
        dept.chief = form.chief.data
        mem_str = form.members.data
        mem_str = mem_str.split()
        for i in mem_str:
            user = db_sess.query(User).filter(User.id == i).first()
            dept.members.append(user)
        dept.email = form.email.data
        db_sess.add(dept)
        db_sess.commit()
        return redirect('/login')
    return render_template('dept_registr.html', title='Регистрация Департамента', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.s_name.data,
            name=form.f_name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            addres=form.addres.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/login")
def login():
    return f'''<h1>Решистрация прошла успешно</h1>'''


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
