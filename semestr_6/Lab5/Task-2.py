from flask import Flask, render_template, redirect
from data import db_session
from data.tables import Job, User
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Job)
    return render_template("index.html", title="Works log", job=job)


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
