from flask import Flask, render_template, redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    userid = StringField('Логин', validators=[DataRequired()])
    password_1 = PasswordField('Пароль', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())

@app.route('/list_prof/<list>')
def list_prof(list):
    proffesions = ['Строитель', 'Инженер', 'Летчик', 'Врач', 'Юрист', 'Управляющий', 'Тренер', 'Стратег', 'Военный']
    return render_template('list_prof.html', list=list.lower(), proffesions=proffesions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')