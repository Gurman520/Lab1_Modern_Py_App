from flask import Flask, render_template, redirect, abort, request
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.tables import Job, User, Department, Category
from forms.user_form import UserForm
from forms.job_form import JobForm
from forms.department_form import DeptForm
from forms.login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Job)
    return render_template("index.html", title="Works log", job=job)


@app.route("/department")
def department_show():
    db_sess = db_session.create_session()
    dept = db_sess.query(Department)
    return render_template("department.html", title="Dept log", dept=dept)


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
        return redirect('/')
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
        return redirect('/department')
    return render_template('dept_registr.html', title='Регистрация Департамента', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = UserForm()
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        use = db_sess.query(User).filter(User.email == form.email.data).first()
        if use and use.check_password(form.password.data):
            login_user(use, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Job).filter(Job.id == id).first()
        if job:
            form.team_leader.data = job.team_leader
            form.job.data = job.job
            form.work_size.data = job.work_size
            colab = ""
            for i in job.collaborators:
                colab += str(i.id) + " "
            form.collaborators.data = colab

            colab = ""
            for i in job.categories:
                colab += str(i.id) + " "
            form.categories.data = colab

            form.start_date.data = job.start_date
            form.end_date.data = job.end_date
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Job).filter(Job.id == id).first()
        if job:
            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.team_leader = form.team_leader.data
            coll_str = form.collaborators.data
            coll_str = coll_str.split()
            for i in coll_str:
                user = db_sess.query(User).filter(User.id == i).first()
                job.collaborators.append(user)

            coll_str = form.categories.data
            coll_str = coll_str.split()
            for i in coll_str:
                cat = db_sess.query(Category).filter(Category.id == i).first()
                job.categories.append(cat)

            if form.is_finished.data is True:
                job.is_finished = True
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job_register.html',
                           title='Редактирование работы', form=form)


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Job).filter(Job.id == id).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/dept_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def depts_delete(id):
    db_sess = db_session.create_session()
    dept = db_sess.query(Department).filter(Department.id == id).first()
    if dept:
        db_sess.delete(dept)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/department')


@app.route('/department/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_dept(id):
    form = DeptForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        dept = db_sess.query(Department).filter(Department.id == id).first()
        if dept:
            form.chief.data = dept.chief
            form.title.data = dept.title
            form.email.data = dept.email
            colab = ""
            for i in dept.members:
                colab += str(i.id) + " "
            form.members.data = colab
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dept = db_sess.query(Department).filter(Department.id == id).first()
        if dept:
            dept.title = form.title.data
            dept.chief = form.chief.data
            dept.email = form.email.data
            coll_str = form.members.data
            coll_str = coll_str.split()
            for i in coll_str:
                user = db_sess.query(User).filter(User.id == i).first()
                dept.members.append(user)
            db_sess.commit()
            return redirect('/department')
        else:
            abort(404)
    return render_template('dept_registr.html', title='Редактирование отдела', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
