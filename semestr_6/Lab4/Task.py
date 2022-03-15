from flask import Flask, json, render_template, redirect, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from loginform import LoginForm
import smtplib

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

prof = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
        "климатолог", "специалист по радиационной защите", "астрогеолог", "инженер жизнеобеспечения"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Добро пожаловать!')


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list.html', title='Список профессий', Prof=prof, li=list)


@app.route('/distribution')
def distribution():
    with open("static/members/Crew.json", "rt", encoding="utf8") as f:
        crew_list = json.loads(f.read())
    return render_template('dist.html', title='Размещение', crew=crew_list)


@app.route('/member/<int:number>')
def member(number):
    with open('static/members/crew.json', encoding='utf8') as js:
        crew = json.load(js)['Crew']
        return render_template('memb_r.html', title='Член экипажа', crew=crew, number=number)


@app.route('/member/random')
def member_random():
    return member('random')


@app.route('/room/<sex>/<int:age>')
def room(sex, age):
    return render_template('room.html', title='Каюты', sex=sex, age=age)


def send_email(to_addr, from_addr, body_text):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(from_addr, "523Rdfhnbhf523")
    server.sendmail(from_addr, to_addr, body_text)
    server.quit()


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form = str(dict(request.form))
        to_addr = request.form['email']
        from_addr = "romanidzs@gmail.com"
        subject = 'Данные формы'
        msg = MIMEMultipart()
        msg['From'] = "romanidzs@gmail.com"
        msg['To'] = request.form['email']
        msg['Subject'] = subject

        msg.attach(MIMEText(form))
        part = MIMEApplication(request.files['photo'].read(), Name=request.files['photo'].filename)
        part['Content-Disposition'] = f'''attachment; filename="{request.files['photo'].filename}"'''
        msg.attach(part)

        send_email(to_addr, from_addr, msg.as_string())
        return redirect('/')

    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
