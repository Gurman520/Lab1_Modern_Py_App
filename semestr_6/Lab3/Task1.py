from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
        <title>Домашняя страница</title> 
    </head>
    <body bgcolor="#A0522D" background="{url_for('static', filename='img/fon.png')}">
        <h1> Наша миссия: Миссия Колонизация Марса </h1>
    </body>
</html>'''


@app.route('/index')
def index():
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
        <title> Девиз </title>
    </head>
    <body bgcolor="#A0522D"> 
    <h1> И на Марсе будут яблони цвести! </h1>
    </body>
</html>'''


@app.route('/promotion')
def promotion():
    advertising = ["Человечество вырастает из детства", "Человечеству мала одна планета",
                   "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br> <h2>'.join(advertising).join('</h2>')


@app.route('/image_mars')
def image_mars():
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
        <title>Привет Марс!</title>
    </head>
    <body bgcolor="#A0522D"> 
    <h1> Жди нас, Марс! </h1> </br>
    <img src="{url_for('static', filename='img/mars.jpg')}" </br>
    <p>Кадр из фильма "Марсианин"</p>
    </body>
</html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <title>Регистрация космонавта</title>
                          </head>
                          <body bgcolor="#A0522D">
                            <h1>Форма для регистрации</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="f_name" class="form-control" id="last_name" " placeholder="Введите фамилию" name="s_name">
                                    <input type="s_name" class="form-control" id="first_name" placeholder="Введите имя" name="f_name">
                                     <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <input type="education" class="form-control" id="education" placeholder="Уровень образования" name="education">
                                    <div class="form-group">
                                        <label for="classSelect">Основная проффесия</label>
                                        <select class="form-control" id="profSelect" name="prof">
                                          <option>инженер-исследователь</option>
                                          <option>пилот</option>
                                          <option>строитель</option>
                                          <option>экзобиолог</option>
                                          <option>врач</option>
                                          <option>инженер по терраформированию</option>
                                          <option>климатолог</option>
                                          <option>специалист по радиационной защите</option>
                                          <option>астрогеолог</option>
                                          <option>гляциолог</option>
                                          <option>инженер жизнеобеспечения</option>
                                          <option>метеоролог</option>
                                          <option>оператор марсохода</option>
                                          <option>киберинженер</option>
                                          <option>штурман</option>
                                          <option>пилот дронов</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="motiv">Мотивация</label>
                                        <textarea class="form-control" id="about" rows="3" name="motiv"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['s_name'])
        print(request.form['f_name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['prof'])
        print(request.form['motiv'])
        print(request.form.get('accept'))
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def greeting(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Астронавт</title>
                  </head>
                  <body bgcolor="#A0522D">
                    <h1>Астронавт, {nickname}!</h1>
                    <h2>Этап отбора: {level}!</h2>
                    <h2>Текущий рэйтинг: {rating}!</h2>
                  </body>
                </html>'''


@app.get('/photo/<nickname>')
def photo_load(nickname):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
<title>Фото астронавта</title>
</head>
    <body bgcolor="#A0522D">
        <h1>Загрузим файл</h1>
    <form method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="photo">Выберете файл</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>>
    </form>
    </body>
</html>'''


@app.post('/photo/<nickname>')
def photo_show(nickname):
    f = request.files['file'].read()
    with open("static/img/" + nickname + ".jpg", "wb") as file:
        file.write(f)
    print("static/img/" + nickname + ".jpg")
    return f'''<!DOCTYPE html>
<html lang="en">
    <body bgcolor="#A0522D">
    <img src="{url_for('static', filename=f'img/{nickname}.jpg')}" />
    </body>
</html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Карусель марса</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style>
    .carousel {{ /*код слайдера размер под разные картики высота*/
  width: 100%;
}}
.carousel-item img {{
  width: 70%;
  height: 500px; /* высота изображения */
  object-fit: cover; /*код слайдера размер под разные картики высота*/
}}
    </style>
</head>
<body bgcolor="#A0522D">
<h1>Фото ладшафта Марса</h1>
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="{url_for('static', filename=f'img/m1.jpg')}" alt="Первый слайд">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename=f'img/m2.jpg')}" alt="Второй слайд">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="{url_for('static', filename=f'img/m3.jpg')}" alt="Третий слайд">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</body> - <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
